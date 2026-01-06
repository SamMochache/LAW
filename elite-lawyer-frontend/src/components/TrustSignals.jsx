import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { api } from "../services/api";

export default function TrustSignals() {
  const [data, setData] = useState({
    achievements: [],
    testimonials: [],
    recognitions: []
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    // Use combined endpoint for better performance
    api.get("/trust-signals/")
      .then(res => {
        setData({
          achievements: res.data.achievements || [],
          testimonials: res.data.testimonials || [],
          recognitions: res.data.recognitions || []
        });
        setLoading(false);
      })
      .catch(err => {
        console.error("Failed to load trust signals:", err);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <section className="px-6 md:px-24 py-32 bg-gradient-to-b from-black/20 via-transparent to-black/20">
        <div className="max-w-6xl mx-auto text-center">
          <div className="flex justify-center">
            <div className="w-8 h-8 border-2 border-champagne border-t-transparent rounded-full animate-spin" />
          </div>
        </div>
      </section>
    );
  }

  if (error) {
    return null; // Silently fail - optional section
  }

  return (
    <section className="px-6 md:px-24 py-32 bg-gradient-to-b from-black/20 via-transparent to-black/20">
      <div className="max-w-6xl mx-auto">
        
        {/* Results Metrics */}
        {data.achievements.length > 0 && (
          <>
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="text-center mb-24"
            >
              <h2 className="font-serif text-4xl md:text-5xl mb-6">
                Track Record of Excellence
              </h2>
              <p className="text-muted text-lg max-w-2xl mx-auto">
                Results that matter to clients who demand the highest standards
              </p>
            </motion.div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 mb-32">
              {data.achievements.map((item, index) => (
                <motion.div
                  key={item.id}
                  initial={{ opacity: 0, y: 30 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="text-center"
                >
                  <div className="mb-4">
                    <div className="text-4xl md:text-5xl font-serif text-champagne mb-2">
                      {item.metric}
                    </div>
                    <div className="text-sm font-medium text-white mb-2">
                      {item.label}
                    </div>
                    <div className="text-xs text-muted">
                      {item.description}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </>
        )}

        {/* Client Testimonials */}
        {data.testimonials.length > 0 && (
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="mb-32"
          >
            <h3 className="font-serif text-3xl text-center mb-16">
              Client Testimonials
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {data.testimonials.map((item, index) => (
                <motion.div
                  key={item.id}
                  initial={{ opacity: 0, y: 30 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="relative p-8 border border-white/10 rounded-lg bg-white/5 backdrop-blur-sm"
                >
                  {/* Quote mark */}
                  <div className="absolute -top-4 left-8">
                    <svg className="w-8 h-8 text-champagne/30" fill="currentColor" viewBox="0 0 32 32">
                      <path d="M10 8v8h-6l3-8h3zm12 0v8h-6l3-8h3z" />
                    </svg>
                  </div>

                  <blockquote className="text-sm leading-relaxed mb-6 text-muted">
                    "{item.quote}"
                  </blockquote>

                  <div className="border-t border-white/10 pt-4">
                    <div className="font-medium text-white text-sm">
                      {item.author}
                    </div>
                    <div className="text-xs text-champagne/70 mt-1">
                      {item.role}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}

        {/* Professional Recognition */}
        {data.recognitions.length > 0 && (
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="text-center"
          >
            <h3 className="font-serif text-3xl mb-12">
              Professional Recognition
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              {data.recognitions.map((item, index) => (
                <motion.div
                  key={item.id}
                  initial={{ opacity: 0, x: index % 2 === 0 ? -20 : 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="flex items-center gap-3 p-4 border border-white/10 rounded-lg bg-white/5"
                >
                  <svg className="w-5 h-5 text-champagne flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                  </svg>
                  <span className="text-sm text-muted text-left">{item.display_text}</span>
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}

      </div>
    </section>
  );
}