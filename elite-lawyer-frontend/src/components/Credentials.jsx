import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { api } from "../services/api";   // axios instance

export default function EnhancedCredentials() {
  const [credentials, setCredentials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    api.get("/credentials/")   // <-- make sure this matches your backend route
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
      <section className="px-6 md:px-24 py-32 bg-gradient-to-b from-transparent to-black/20">
        <div className="max-w-5xl mx-auto">
          <h2 className="font-serif text-4xl mb-16 text-center">
            Credentials & Qualifications
          </h2>
          <div className="flex justify-center">
            <div className="w-8 h-8 border-2 border-champagne border-t-transparent rounded-full animate-spin" />
          </div>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="px-6 md:px-24 py-32">
        <h2 className="font-serif text-4xl mb-8 text-center">
          Credentials & Qualifications
        </h2>
        <p className="text-center text-muted">
          Unable to load credentials right now.
        </p>
      </section>
    );
  }

  return (
    <section id="credentials" className="px-6 md:px-24 py-32 bg-gradient-to-b from-transparent via-black/20 to-transparent">
      <div className="max-w-5xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-20"
        >
          <h2 className="font-serif text-4xl md:text-5xl mb-6">
            Credentials & Qualifications
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Academic excellence and professional distinction earned through decades of legal practice
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {credentials.map((cred, index) => (
            <motion.div
              key={cred.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              className="group relative"
            >
              <div className="absolute inset-0 bg-gradient-to-br from-champagne/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg" />

              <div className="relative p-8 border border-white/10 rounded-lg backdrop-blur-sm hover:border-champagne/30 transition-all duration-300">
                <div className="absolute -top-4 right-8">
                  <span className="inline-block px-4 py-1 bg-champagne/10 border border-champagne/30 rounded-full text-champagne text-sm font-medium">
                    {cred.year || "N/A"}
                  </span>
                </div>

                <div className="space-y-3 mt-2">
                  <h3 className="text-xl font-medium text-white group-hover:text-champagne transition-colors duration-300">
                    {cred.title}
                  </h3>

                  <p className="text-muted font-light">
                    {cred.institution}
                  </p>
                </div>

                <div className="mt-6 h-px bg-gradient-to-r from-champagne/0 via-champagne/30 to-champagne/0" />
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="mt-20 text-center"
        >
          <div className="inline-flex flex-wrap gap-6 justify-center text-sm text-muted">
            <span className="px-4 py-2 border border-white/10 rounded-full">
              7+ Years Experience
            </span>
            <span className="px-4 py-2 border border-white/10 rounded-full">
              Senior Advocate
            </span>
            <span className="px-4 py-2 border border-white/10 rounded-full">
              International Recognition
            </span>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
