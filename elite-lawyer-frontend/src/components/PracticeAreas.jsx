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
  <section id="practice" className="px-6 md:px-24 py-24 md:py-32">
    <h2 className="font-serif text-3xl md:text-4xl mb-12 md:mb-16">
      Practice Areas
    </h2>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12 md:gap-16">
      {areas.map(area => (
        <div
          key={area.id}
          className="space-y-4 md:space-y-6"
        >
          <h3 className="text-lg md:text-xl font-medium">
            {area.title}
          </h3>

          <p className="text-muted leading-relaxed">
            {area.description}
          </p>
        </div>
      ))}
    </div>
  </section>
);

}
