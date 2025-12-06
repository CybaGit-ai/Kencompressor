import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { getListingIntel } from '../api';
import { initWebLLM, runWebLLMReport, LLMReport } from '../webllmClient';
import ChartsPanel from '../components/ChartsPanel';
import WebLLMInsightsPanel from '../components/WebLLMInsightsPanel';

export default function ListingIntelPage() {
  const { id } = useParams();
  const [llmReport, setLlmReport] = useState<LLMReport | null>(null);

  const { data, isLoading, error } = useQuery({
    queryKey: ['intel', id],
    queryFn: () => getListingIntel(id || ''),
    enabled: !!id,
  });

  useEffect(() => {
    async function run() {
      if (!data?.intel_json) return;
      await initWebLLM();
      const report = await runWebLLMReport(data.intel_json);
      setLlmReport(report);
    }
    run();
  }, [data]);

  if (isLoading) return <div className="container">Loading...</div>;
  if (error) return <div className="container">Unable to load intel.</div>;

  const intel = data?.intel_json;
  if (!intel) return null;

  const listing = intel.listing;
  const metrics = intel.metrics;

  return (
    <div className="container">
      <div className="card">
        <h2>{listing.address}</h2>
        <p>
          {listing.city} • ${listing.price.toLocaleString()} • {listing.beds} bd / {listing.baths} ba • {listing.sqft} sqft
        </p>
        <p>
          Agent: {listing.agent.name} ({listing.agent.phone}) – {listing.agent.brokerage}
        </p>
        <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
          <span className="badge">Livability {metrics.scores.livability}</span>
          <span className="badge">Transit {metrics.scores.transit}</span>
          <span className="badge">Walk {metrics.scores.walkability}</span>
          <span className="badge">Schools {metrics.scores.schools}</span>
          <span className="badge">Investment {metrics.scores.investment}</span>
        </div>
      </div>

      <div className="card">
        <h3>Market Snapshot</h3>
        <p>
          Median price in {metrics.market.area}: ${metrics.market.median_price_area.toLocaleString()} (DOM {metrics.market.avg_days_on_market_area})
        </p>
        <p>YOY change: {metrics.market.yoy_price_change_area}% • Sale-to-list: {metrics.market.sale_to_list_ratio_area}</p>
      </div>

      <div className="card">
        <h3>Location Metrics</h3>
        <p>Amenities within 1km: {metrics.amenities.within_1km.parks} parks, {metrics.amenities.within_1km.grocery} grocery, {metrics.amenities.within_1km.restaurants} restaurants.</p>
        <p>Routes: {metrics.routes.downtown_abbotsford_drive_min} min to Downtown Abbotsford, {metrics.routes.downtown_vancouver_drive_min} min to Vancouver.</p>
        <p>Environment: Floodplain {metrics.environment.in_floodplain ? 'yes' : 'no'}, ALR {metrics.environment.in_alr ? 'yes' : 'no'}.</p>
      </div>

      <WebLLMInsightsPanel report={llmReport} />
      <ChartsPanel intel={intel} chartSpecs={llmReport?.charts || []} />
    </div>
  );
}
