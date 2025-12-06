import { Link } from 'react-router-dom';

export default function LandingPage() {
  return (
    <div className="container">
      <div className="card">
        <h1>Fraser Valley Agent Intel</h1>
        <p>
          AI + data for Fraser Valley properties. Instantly blend GIS layers, market stats, climate, and amenities into one
          intelligence view for BC agents.
        </p>
        <Link to="/agent" className="button">
          I'm an agent – view my listings
        </Link>
      </div>
      <div className="card">
        <h3>What you get</h3>
        <ul>
          <li>Unified municipal + provincial GIS overlays.</li>
          <li>Market momentum, DOM, and price history charts.</li>
          <li>Browser-side AI (webLLM) summarizing the intel JSON.</li>
        </ul>
      </div>
    </div>
  );
}
