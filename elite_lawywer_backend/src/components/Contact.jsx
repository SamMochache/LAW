import { useState } from "react";
import { motion } from "framer-motion";
import { api } from "../services/api";

export default function EliteContact() {
  const [formData, setFormData] = useState({
    fullName: "",
    company: "",
    email: "",
    phone: "",
    matterType: "",
    urgency: "standard",
    details: "",
    referralSource: ""
  });

  const [status, setStatus] = useState({ type: "", message: "" });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    // Clear error for this field when user starts typing
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: "" }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    setStatus({ type: "", message: "" });
    setErrors({});

    // Client-side validation
    const newErrors = {};
    if (formData.details.length < 100) {
      newErrors.details = "Please provide at least 100 characters describing your matter.";
    }
    if (!formData.email.includes("@")) {
      newErrors.email = "Please provide a valid email address.";
    }
    if (formData.phone.length < 10) {
      newErrors.phone = "Please provide a valid phone number.";
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      setIsSubmitting(false);
      return;
    }

    try {
      // Map camelCase to snake_case for Django API
      const payload = {
        full_name: formData.fullName,
        company: formData.company,
        email: formData.email,
        phone: formData.phone,
        matter_type: formData.matterType,
        urgency: formData.urgency,
        details: formData.details,
        referral_source: formData.referralSource,
      };

      console.log("Sending payload:", payload); // Debug log

      const response = await api.post("/contact/", payload);
      
      console.log("Response:", response.data); // Debug log

      setStatus({
        type: "success",
        message: "Thank you. Your inquiry has been received and will be reviewed within 24 hours.",
      });

      // Reset form
      setFormData({
        fullName: "",
        company: "",
        email: "",
        phone: "",
        matterType: "",
        urgency: "standard",
        details: "",
        referralSource: "",
      });

      // Scroll to success message
      setTimeout(() => {
        document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" });
      }, 100);

    } catch (error) {
      console.error("Submission error:", error);
      
      // Handle validation errors from backend
      if (error.response?.data) {
        const backendErrors = error.response.data;
        const formattedErrors = {};
        
        // Convert snake_case backend errors to camelCase for frontend
        Object.keys(backendErrors).forEach(key => {
          const camelKey = key.replace(/_([a-z])/g, (g) => g[1].toUpperCase());
          formattedErrors[camelKey] = Array.isArray(backendErrors[key]) 
            ? backendErrors[key][0] 
            : backendErrors[key];
        });
        
        setErrors(formattedErrors);
        setStatus({
          type: "error",
          message: "Please correct the errors below and try again.",
        });
      } else {
        setStatus({
          type: "error",
          message: "Unable to submit inquiry. Please contact us directly via phone or try again later.",
        });
      }
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section
      id="contact"
      className="px-6 md:px-24 py-32 bg-gradient-to-b from-black/20 to-transparent"
    >
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h2 className="font-serif text-4xl md:text-5xl mb-6">
            Consultation Request
          </h2>
          <p className="text-muted text-lg max-w-2xl mx-auto">
            Consultations are offered selectively based on matter complexity
            and suitability. Provide detailed information for prompt evaluation.
          </p>
        </motion.div>

        <motion.form
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.2 }}
          onSubmit={handleSubmit}
          className="space-y-8"
        >
          {/* Personal Info */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="fullName" className="block text-sm font-medium mb-2">
                Full Name <span className="text-champagne">*</span>
              </label>
              <input
                type="text"
                id="fullName"
                name="fullName"
                value={formData.fullName}
                onChange={handleChange}
                required
                placeholder="John Doe"
                className={`w-full px-4 py-3 bg-white/5 border rounded-lg focus:outline-none focus:ring-1 transition-all ${
                  errors.fullName 
                    ? 'border-red-500 focus:border-red-500 focus:ring-red-500/30' 
                    : 'border-white/10 focus:border-champagne/50 focus:ring-champagne/30'
                }`}
              />
              {errors.fullName && (
                <p className="mt-1 text-sm text-red-400">{errors.fullName}</p>
              )}
            </div>
            <div>
              <label htmlFor="company" className="block text-sm font-medium mb-2">
                Company / Organization
              </label>
              <input
                type="text"
                id="company"
                name="company"
                value={formData.company}
                onChange={handleChange}
                placeholder="Optional"
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg focus:border-champagne/50 focus:outline-none focus:ring-1 focus:ring-champagne/30 transition-all"
              />
            </div>
          </div>

          {/* Contact Info */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="email" className="block text-sm font-medium mb-2">
                Email Address <span className="text-champagne">*</span>
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                placeholder="john@example.com"
                className={`w-full px-4 py-3 bg-white/5 border rounded-lg focus:outline-none focus:ring-1 transition-all ${
                  errors.email 
                    ? 'border-red-500 focus:border-red-500 focus:ring-red-500/30' 
                    : 'border-white/10 focus:border-champagne/50 focus:ring-champagne/30'
                }`}
              />
              {errors.email && (
                <p className="mt-1 text-sm text-red-400">{errors.email}</p>
              )}
            </div>
            <div>
              <label htmlFor="phone" className="block text-sm font-medium mb-2">
                Phone Number <span className="text-champagne">*</span>
              </label>
              <input
                type="tel"
                id="phone"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                required
                placeholder="+254 XXX XXX XXX"
                className={`w-full px-4 py-3 bg-white/5 border rounded-lg focus:outline-none focus:ring-1 transition-all ${
                  errors.phone 
                    ? 'border-red-500 focus:border-red-500 focus:ring-red-500/30' 
                    : 'border-white/10 focus:border-champagne/50 focus:ring-champagne/30'
                }`}
              />
              {errors.phone && (
                <p className="mt-1 text-sm text-red-400">{errors.phone}</p>
              )}
            </div>
          </div>

          {/* Matter Info */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="matterType" className="block text-sm font-medium mb-2">
                Type of Legal Matter <span className="text-champagne">*</span>
              </label>
              <select
                id="matterType"
                name="matterType"
                value={formData.matterType}
                onChange={handleChange}
                required
                className={`w-full px-4 py-3 bg-white/5 border rounded-lg focus:outline-none focus:ring-1 transition-all ${
                  errors.matterType 
                    ? 'border-red-500 focus:border-red-500 focus:ring-red-500/30' 
                    : 'border-white/10 focus:border-champagne/50 focus:ring-champagne/30'
                }`}
              >
                <option value="">Select matter type</option>
                <option value="corporate">Corporate & Commercial</option>
                <option value="litigation">Commercial Litigation</option>
                <option value="tax">Tax Advisory</option>
                <option value="real-estate">Real Estate & Property</option>
                <option value="employment">Employment Law</option>
                <option value="intellectual">Intellectual Property</option>
                <option value="regulatory">Regulatory Compliance</option>
                <option value="other">Other (specify in details)</option>
              </select>
              {errors.matterType && (
                <p className="mt-1 text-sm text-red-400">{errors.matterType}</p>
              )}
            </div>
            <div>
              <label htmlFor="urgency" className="block text-sm font-medium mb-2">
                Urgency Level
              </label>
              <select
                id="urgency"
                name="urgency"
                value={formData.urgency}
                onChange={handleChange}
                className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg focus:border-champagne/50 focus:outline-none focus:ring-1 focus:ring-champagne/30 transition-all"
              >
                <option value="standard">Standard (1-2 weeks)</option>
                <option value="priority">Priority (3-5 days)</option>
                <option value="urgent">Urgent (24-48 hours)</option>
              </select>
            </div>
          </div>

          {/* Details */}
          <div>
            <label htmlFor="details" className="block text-sm font-medium mb-2">
              Brief Description of Matter <span className="text-champagne">*</span>
            </label>
            <textarea
              id="details"
              name="details"
              value={formData.details}
              onChange={handleChange}
              required
              rows={6}
              placeholder="Provide a detailed description of your legal matter... (minimum 100 characters)"
              className={`w-full px-4 py-3 bg-white/5 border rounded-lg focus:outline-none focus:ring-1 transition-all resize-none ${
                errors.details 
                  ? 'border-red-500 focus:border-red-500 focus:ring-red-500/30' 
                  : 'border-white/10 focus:border-champagne/50 focus:ring-champagne/30'
              }`}
            />
            <div className="flex justify-between items-center mt-2">
              <p className="text-xs text-muted">
                All communications are protected by attorney-client privilege.
              </p>
              <p className={`text-xs ${formData.details.length >= 100 ? 'text-green-400' : 'text-muted'}`}>
                {formData.details.length}/100 characters
              </p>
            </div>
            {errors.details && (
              <p className="mt-1 text-sm text-red-400">{errors.details}</p>
            )}
          </div>

          {/* Referral */}
          <div>
            <label htmlFor="referralSource" className="block text-sm font-medium mb-2">
              How did you hear about us?
            </label>
            <input
              type="text"
              id="referralSource"
              name="referralSource"
              value={formData.referralSource}
              onChange={handleChange}
              placeholder="Referral, search engine, professional network, etc."
              className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg focus:border-champagne/50 focus:outline-none focus:ring-1 focus:ring-champagne/30 transition-all"
            />
          </div>

          {/* Status Message */}
          {status.message && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              className={`p-4 rounded-lg border ${
                status.type === "success"
                  ? "bg-green-500/10 border-green-500/30 text-green-400"
                  : "bg-red-500/10 border-red-500/30 text-red-400"
              }`}
            >
              <p className="font-medium">{status.message}</p>
            </motion.div>
          )}

          {/* Submit Button */}
          <div className="flex justify-center pt-4">
            <button
              type="submit"
              disabled={isSubmitting}
              className="group relative px-12 py-4 bg-champagne text-black font-medium rounded-lg hover:bg-champagne/90 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed overflow-hidden"
            >
              <span className="relative z-10">
                {isSubmitting ? "Submitting..." : "Submit Consultation Request"}
              </span>
              <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700" />
            </button>
          </div>
        </motion.form>
      </div>
    </section>
  );
}