import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function Philosophy() {
  const [text, setText] = useState("");

  useEffect(() => {
    api.get("/philosophy/")
      .then(res => setText(res.data.body));
  }, []);

  return (
    <section className="px-24 max-w-3xl">
      <h2 className="font-serif text-4xl mb-12">
        Legal Ethos
      </h2>

      <p className="text-lg leading-relaxed text-muted">
        {text}
      </p>
    </section>
  );
}
