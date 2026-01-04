import { useEffect, useState } from "react";
import { api } from "../services/api";  // your axios instance

export default function Credentials() {
  const [credentials, setCredentials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    api.get("/credentials/")  // Make sure this matches your backend route
      .then(res => {
        const data = Array.isArray(res.data) ? res.data : [];
        setCredentials(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load credentials:", err);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Credentials</h2>
        <p className="text-muted">Loading credentials...</p>
      </section>
    );
  }

  if (error) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Credentials</h2>
        <p className="text-muted">Unable to load credentials at this time.</p>
      </section>
    );
  }

  if (credentials.length === 0) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Credentials</h2>
        <p className="text-muted">No credentials found.</p>
      </section>
    );
  }

  return (
    <section className="px-24">
      <h2 className="font-serif text-4xl mb-16">Credentials</h2>

      <ul className="list-disc list-inside space-y-2">
        {credentials.map(({ id, title, institution, year }) => (
          <li key={id}>
            <strong>{title}</strong> — {institution} ({year || "N/A"})
          </li>
        ))}
      </ul>
    </section>
  );
}
