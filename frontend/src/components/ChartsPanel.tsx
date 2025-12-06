import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Bar, BarChart, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, Legend } from 'recharts';
import { LLMChartSpec } from '../webllmClient';

interface Props {
  intel: any;
  chartSpecs: LLMChartSpec[];
}

export default function ChartsPanel({ intel, chartSpecs }: Props) {
  const getDataForSource = (source: string) => {
    const segments = source.split('.');
    return segments.reduce((acc: any, key: string) => (acc ? acc[key] : undefined), intel);
  };

  return (
    <div>
      {chartSpecs.map((spec) => {
        const data = getDataForSource(spec.source) || [];
        if (spec.type === 'line') {
          return (
            <div key={spec.id} className="card">
              <h4>{spec.title}</h4>
              <LineChart width={500} height={250} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey={spec.x_field} />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey={spec.y_field || ''} stroke="#0ea5e9" />
              </LineChart>
            </div>
          );
        }
        if (spec.type === 'bar') {
          return (
            <div key={spec.id} className="card">
              <h4>{spec.title}</h4>
              <BarChart width={500} height={250} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey={spec.x_field} />
                <YAxis />
                <Tooltip />
                <Bar dataKey={spec.y_field || ''} fill="#22c55e" />
              </BarChart>
            </div>
          );
        }
        if (spec.type === 'radar') {
          const radarData = (spec.fields || []).map((field) => ({ metric: field, value: intel.metrics.scores[field] }));
          return (
            <div key={spec.id} className="card">
              <h4>{spec.title}</h4>
              <RadarChart outerRadius={90} width={500} height={300} data={radarData}>
                <PolarGrid />
                <PolarAngleAxis dataKey="metric" />
                <PolarRadiusAxis angle={30} domain={[0, 100]} />
                <Radar name="Scores" dataKey="value" stroke="#8b5cf6" fill="#8b5cf6" fillOpacity={0.6} />
                <Legend />
              </RadarChart>
            </div>
          );
        }
        return null;
      })}
    </div>
  );
}
