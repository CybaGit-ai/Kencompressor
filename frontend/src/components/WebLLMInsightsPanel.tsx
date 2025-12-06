import { LLMReport } from '../webllmClient';

interface Props {
  report: LLMReport | null;
}

export default function WebLLMInsightsPanel({ report }: Props) {
  if (!report) return null;

  return (
    <div className="card">
      <h3>AI Insights</h3>
      <div>
        <h4>Summary</h4>
        <ul>
          {report.summary_bullets.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <h4>Talking Points</h4>
        <ul>
          {report.talking_points.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <h4>Social Captions</h4>
        <ul>
          {report.social_captions.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
