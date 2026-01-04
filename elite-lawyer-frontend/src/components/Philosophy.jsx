import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function Philosophy() {
  const [text, setText] = useState("");

  useEffect(() => {
    api.get("/philosophy/")
      .then(res => setText(res.data.body));
  }, []);

  return (
    <section id="ethos" className="px-6 md:px-24 py-32 max-w-3xl">
      <h2 className="font-serif text-4xl mb-12">
        Legal Ethos
      </h2>

      <p className="text-lg leading-relaxed text-muted">
        {text}
      </p>
    </section>
  );
}
