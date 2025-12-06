import { FormEvent, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { resolveAgent } from '../api';

export default function AgentPortalPage() {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [searchParams, setSearchParams] = useState<{ name: string; phone: string } | null>(null);
  const navigate = useNavigate();

  const { data, error } = useQuery({
    queryKey: ['agents', searchParams],
    queryFn: () => resolveAgent(searchParams?.name ?? '', searchParams?.phone ?? ''),
    enabled: !!searchParams,
  });

  const onSubmit = (e: FormEvent) => {
    e.preventDefault();
    setSearchParams({ name, phone });
  };

  const onChoose = (agentId: string) => {
    navigate(`/agent/${agentId}/listings`);
  };

  return (
    <div className="container">
      <div className="card">
        <h2>Agent Portal</h2>
        <form onSubmit={onSubmit}>
          <div>
            <label>Name</label>
            <br />
            <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Alex" />
          </div>
          <div>
            <label>Phone</label>
            <br />
            <input value={phone} onChange={(e) => setPhone(e.target.value)} placeholder="604" />
          </div>
          <div style={{ marginTop: 12 }}>
            <button className="button" type="submit">
              Resolve agent
            </button>
          </div>
        </form>
        {error && <p style={{ color: 'red' }}>No matching agents found.</p>}
      </div>

      {data && (
        <div className="card">
          <h3>Select your profile</h3>
          <ul>
            {data.map((agent: any) => (
              <li key={agent.id} style={{ marginBottom: 8 }}>
                <span style={{ marginRight: 12 }}>
                  {agent.name} ({agent.phone}) – {agent.brokerage}
                </span>
                <button className="button" onClick={() => onChoose(agent.id)}>
                  View listings
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
