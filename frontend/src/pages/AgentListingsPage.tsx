import { useParams, Link } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { getAgentListings } from '../api';

export default function AgentListingsPage() {
  const { id } = useParams();
  const { data, isLoading, error } = useQuery({
    queryKey: ['listings', id],
    queryFn: () => getAgentListings(id || ''),
    enabled: !!id,
  });

  return (
    <div className="container">
      <div className="card">
        <h2>My Active Listings</h2>
        {isLoading && <p>Loading...</p>}
        {error && <p style={{ color: 'red' }}>Unable to load listings.</p>}
        {data && (
          <table className="table">
            <thead>
              <tr>
                <th>Address</th>
                <th>City</th>
                <th>Price</th>
                <th>Beds</th>
                <th>Baths</th>
                <th>Type</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {data.map((listing: any) => (
                <tr key={listing.id}>
                  <td>{listing.address}</td>
                  <td>{listing.city}</td>
                  <td>${listing.price.toLocaleString()}</td>
                  <td>{listing.beds}</td>
                  <td>{listing.baths}</td>
                  <td>{listing.property_type}</td>
                  <td>
                    <Link to={`/listing/${listing.id}`} className="button">
                      View AI report
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
