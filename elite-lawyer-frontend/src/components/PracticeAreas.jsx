import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function PracticeAreas() {
  const [areas, setAreas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    api.get("/practice-areas/")
      .then(res => {
        // Defensive: only set if data is an array, else empty array
        const data = Array.isArray(res.data) ? res.data : [];
        setAreas(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load practice areas:", err);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Practice Areas</h2>
        <p className="text-muted">Loading practice areas...</p>
      </section>
    );
  }

  if (error) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Practice Areas</h2>
        <p className="text-muted">Unable to load practice areas at this time.</p>
      </section>
    );
  }

  if (areas.length === 0) {
    return (
      <section className="px-24">
        <h2 className="font-serif text-4xl mb-16">Practice Areas</h2>
        <p className="text-muted">No practice areas available yet.</p>
      </section>
    );
  }

  return (
    <section className="px-24">
      <h2 className="font-serif text-4xl mb-16">Practice Areas</h2>

      <div className="grid grid-cols-3 gap-16">
        {areas.map(area => (
          <div key={area.id}>
            <h3 className="text-xl mb-4">{area.title}</h3>
            <p className="text-muted">{area.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
