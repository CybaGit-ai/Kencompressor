import { FormEvent, useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useMutation, useQuery } from '@tanstack/react-query';
import { createListingForAgent, getAgentListings } from '../api';

export default function AgentListingsPage() {
  const { id } = useParams();
  const [listings, setListings] = useState<any[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({
    address: '',
    city: '',
    region: '',
    price: '',
    beds: '',
    baths: '',
    property_type: '',
  });
  const { data, isLoading, error } = useQuery({
    queryKey: ['listings', id],
    queryFn: () => getAgentListings(id || ''),
    enabled: !!id,
  });

  useEffect(() => {
    if (data) {
      setListings(data);
    }
  }, [data]);

  const createMutation = useMutation({
    mutationFn: (payload: any) => createListingForAgent(id || '', payload),
    onSuccess: (newListing) => {
      setListings((prev) => [...prev, newListing]);
      setForm({
        address: '',
        city: '',
        region: '',
        price: '',
        beds: '',
        baths: '',
        property_type: '',
      });
      setShowForm(false);
    },
  });

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!id) return;
    createMutation.mutate({
      address: form.address,
      city: form.city,
      region: form.region,
      price: parseInt(form.price, 10),
      beds: parseInt(form.beds, 10),
      baths: parseFloat(form.baths),
      property_type: form.property_type,
    });
  };

  return (
    <div className="container">
      <div className="card">
        <h2>My Active Listings</h2>
        <button className="button" onClick={() => setShowForm((prev) => !prev)}>
          {showForm ? 'Cancel' : 'Add Property'}
        </button>
        {showForm && (
          <form className="form" onSubmit={handleSubmit} style={{ marginTop: '1rem' }}>
            <div className="form-row">
              <label>Address</label>
              <input
                value={form.address}
                onChange={(e) => setForm({ ...form, address: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>City</label>
              <input
                value={form.city}
                onChange={(e) => setForm({ ...form, city: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>Region</label>
              <input
                value={form.region}
                onChange={(e) => setForm({ ...form, region: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>Price</label>
              <input
                type="number"
                value={form.price}
                onChange={(e) => setForm({ ...form, price: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>Beds</label>
              <input
                type="number"
                value={form.beds}
                onChange={(e) => setForm({ ...form, beds: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>Baths</label>
              <input
                type="number"
                step="0.5"
                value={form.baths}
                onChange={(e) => setForm({ ...form, baths: e.target.value })}
                required
              />
            </div>
            <div className="form-row">
              <label>Property Type</label>
              <input
                value={form.property_type}
                onChange={(e) => setForm({ ...form, property_type: e.target.value })}
                required
              />
            </div>
            <button className="button" type="submit" disabled={createMutation.isPending}>
              {createMutation.isPending ? 'Creating...' : 'Save Listing'}
            </button>
            {createMutation.error && (
              <p style={{ color: 'red' }}>Unable to create listing. Please try again.</p>
            )}
          </form>
        )}
        {isLoading && <p>Loading...</p>}
        {error && <p style={{ color: 'red' }}>Unable to load listings.</p>}
        {listings && listings.length > 0 && (
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
              {listings.map((listing: any) => (
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
