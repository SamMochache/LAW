import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section className="min-h-screen flex items-center px-24">
      <div className="grid grid-cols-2 gap-24 items-center w-full">

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="font-serif text-6xl leading-tight">
            Senior Advocate of the High Court of Kenya
          </h1>

          <p className="mt-8 text-muted max-w-md">
            Advising executives, institutions, and private clients on
            complex legal matters with discretion and precision.
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1.2 }}
          className="relative h-[640px] flex items-end justify-center"
        >
          {/* Soft background frame */}
  <div className="absolute inset-0 bg-gradient-to-b from-transparent via-black/40 to-black/70" />
        <img
            src="/senior lawyer.png"
            alt="Senior Advocate of the High Court of Kenya"
            className="relative max-h-full object-contain drop-shadow-[0_30px_60px_rgba(0,0,0,0.6)]"
          />
        </motion.div>

      </div>
    </section>
  );
}
