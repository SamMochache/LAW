import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function Experience() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    api.get("/experience/")
      .then(res => {
        const data = Array.isArray(res.data) ? res.data : [];
        setItems(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load experience:", err);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <section className="px-24 max-w-4xl">
        <h2 className="font-serif text-4xl mb-16">Selected Matters</h2>
        <p className="text-muted">Loading selected matters...</p>
      </section>
    );
  }

  if (error) {
    return (
      <section className="px-24 max-w-4xl">
        <h2 className="font-serif text-4xl mb-16">Selected Matters</h2>
        <p className="text-muted">Unable to load selected matters at this time.</p>
      </section>
    );
  }

  if (items.length === 0) {
    return (
      <section className="px-24 max-w-4xl">
        <h2 className="font-serif text-4xl mb-16">Selected Matters</h2>
        <p className="text-muted">No selected matters available yet.</p>
      </section>
    );
  }

  return (
    <section className="px-24 max-w-4xl">
      <h2 className="font-serif text-4xl mb-16">Selected Matters</h2>

      <div className="space-y-12">
        {items.map(item => (
          <div key={item.id}>
            <h3 className="text-xl mb-2">{item.title}</h3>
            <p className="text-muted">{item.summary}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
