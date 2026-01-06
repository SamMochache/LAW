import Hero from "../components/Hero";
import About from "../components/About";
import PracticeAreas from "../components/PracticeAreas";
import Experience from "../components/Experience";
import Credentials from "../components/Credentials";
import Philosophy from "../components/Philosophy";
import Contact from "../components/Contact";
import TrustSignals from "../components/TrustSignals";

export default function Home() {
  return (
    <main className="space-y-40">
      <Hero />
      <About />
      <PracticeAreas />
      <TrustSignals />
      <Experience />
      <Credentials />
      <Philosophy />
      <Contact />
    </main>
  );
}
