const API_BASE = 'http://localhost:8000';

export async function resolveAgent(name: string, phone: string) {
  const url = new URL(`${API_BASE}/agent/resolve`);
  if (name) url.searchParams.append('name', name);
  if (phone) url.searchParams.append('phone', phone);
  const res = await fetch(url.toString());
  if (!res.ok) throw new Error('Agent not found');
  return res.json();
}

export async function getAgentListings(agentId: string) {
  const res = await fetch(`${API_BASE}/agent/${agentId}/listings`);
  if (!res.ok) throw new Error('Listings not found');
  return res.json();
}

export async function createListingForAgent(agentId: string, payload: any) {
  const res = await fetch(`${API_BASE}/agent/${agentId}/listings`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error('Failed to create listing');
  return res.json();
}

export async function getListingIntel(listingId: string) {
  const res = await fetch(`${API_BASE}/listing/${listingId}/intel`);
  if (!res.ok) throw new Error('Intel not found');
  return res.json();
}
