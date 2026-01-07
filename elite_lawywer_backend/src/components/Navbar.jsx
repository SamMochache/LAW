import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function Navbar() {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Top bar */}
      <header className="fixed top-0 left-0 right-0 z-50 px-6 py-4 md:px-24
  bg-black/60 backdrop-blur-md border-b border-white/5">

        <div className="flex items-center justify-between">
          <span className="font-serif text-lg tracking-wide">
            Richard Nyamwange
          </span>

          {/* Mobile menu button */}
          <button
            className="md:hidden text-sm tracking-wide"
            onClick={() => setOpen(true)}
          >
            Menu
          </button>
        </div>
      </header>

      {/* Mobile overlay */}
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 bg-black/95 flex flex-col px-8"
          >
            <button
              className="absolute top-6 right-6 text-sm"
              onClick={() => setOpen(false)}
            >
              Close
            </button>

            <nav className="flex flex-col justify-center flex-1 space-y-12 text-3xl font-serif leading-snug">
              <a href="#about" onClick={() => setOpen(false)}>About</a>
              <a href="#practice" onClick={() => setOpen(false)}>Practice</a>
              <a href="#ethos" onClick={() => setOpen(false)}>Ethos</a>
              <a href="#experience" onClick={() => setOpen(false)}>Experience</a>
              <a href="#credentials" onClick={() => setOpen(false)}>Credentials</a>
              <a href="#contact" onClick={() => setOpen(false)}>Contact</a>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
