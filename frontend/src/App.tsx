import { Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import AgentPortalPage from './pages/AgentPortalPage';
import AgentListingsPage from './pages/AgentListingsPage';
import ListingIntelPage from './pages/ListingIntelPage';

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/agent" element={<AgentPortalPage />} />
      <Route path="/agent/:id/listings" element={<AgentListingsPage />} />
      <Route path="/listing/:id" element={<ListingIntelPage />} />
    </Routes>
  );
}

export default App;
