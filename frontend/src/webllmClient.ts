export type LLMChartSpec = {
  id: string;
  type: 'line' | 'bar' | 'radar';
  title: string;
  x_field?: string;
  y_field?: string;
  fields?: string[];
  source: string;
};

export type LLMReport = {
  summary_bullets: string[];
  talking_points: string[];
  social_captions: string[];
  charts: LLMChartSpec[];
};

export async function initWebLLM(): Promise<void> {
  // In a real integration we would warm up the model here.
  return Promise.resolve();
}

export async function runWebLLMReport(intel: any): Promise<LLMReport> {
  // System prompt example:
  // "You are a real estate intelligence assistant for Fraser Valley BC. You receive JSON called 'intel' describing one property and its metrics. Output STRICT JSON matching the TypeScript type LLMReport. Do not output markdown, comments, or anything except JSON."
  // User prompt example:
  // "Here is the intel JSON for the property: <intel as JSON>"

  const metrics = intel.metrics;
  const listing = intel.listing;

  const summary_bullets = [
    `Asking $${listing.price.toLocaleString()} for ${listing.beds} bed/${listing.baths} bath ${listing.property_type}.`,
    `Livability ${metrics.scores.livability}/100 with schools ${metrics.scores.schools}/100.`,
    `Transit score ${metrics.scores.transit} and walkability ${metrics.scores.walkability}.`,
    `Median price in ${metrics.market.area} is $${metrics.market.median_price_area.toLocaleString()} with DOM ${metrics.market.avg_days_on_market_area}.`,
  ];

  const talking_points = [
    `Area YOY change ${metrics.market.yoy_price_change_area}% with sale-to-list ${metrics.market.sale_to_list_ratio_area}.`,
    `Amenity density: ${metrics.amenities.within_1km.parks} parks and ${metrics.amenities.within_1km.restaurants} restaurants within 1km.`,
    `Drive to Vancouver ~${metrics.routes.downtown_vancouver_drive_min} minutes, SkyTrain ~${metrics.routes.nearest_skytrain_drive_min} minutes.`,
    `Environment: ALR ${metrics.environment.in_alr}, floodplain ${metrics.environment.in_floodplain}.`,
  ];

  const social_captions = [
    `${listing.address}: $${listing.price.toLocaleString()} | ${listing.beds}bd ${listing.baths}ba · ${listing.sqft} sqft #fraservalley #realestate`,
    `Touring ${listing.address} in ${metrics.market.area}! Great investment score ${metrics.scores.investment}.`,
    `Lifestyle + transit balance at ${listing.address} with walk score ${metrics.scores.walkability}.`,
  ];

  const charts: LLMChartSpec[] = [
    {
      id: 'price-history',
      type: 'line',
      title: 'Area Median Price',
      x_field: 'month',
      y_field: 'median_price',
      source: 'time_series.area_price_history',
    },
    {
      id: 'dom-history',
      type: 'bar',
      title: 'Days on Market',
      x_field: 'month',
      y_field: 'avg_dom',
      source: 'time_series.area_dom_history',
    },
    {
      id: 'scores-radar',
      type: 'radar',
      title: 'Score Radar',
      fields: ['livability', 'transit', 'walkability', 'schools', 'investment'],
      source: 'metrics.scores',
    },
  ];

  return { summary_bullets, talking_points, social_captions, charts };
}
