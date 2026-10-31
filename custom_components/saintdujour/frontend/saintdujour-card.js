/* Carte Lovelace « Saint du jour » — livrée avec l'intégration saintdujour. */
(() => {
  const DEFAULTS = {
    title: "🙏 Saints du jour",
    entity_today: "sensor.saint_du_jour",
    entity_tomorrow: "sensor.saint_de_demain",
    label_today: "Saint du jour",
    label_tomorrow: "Saint de demain",
    icon: "🙏",
    show_tomorrow: true,
  };

  const esc = (v) =>
    String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  class SaintDuJourCard extends HTMLElement {
    static getConfigForm() {
      return {
        schema: [
          { name: "title", selector: { text: {} } },
          {
            type: "grid",
            name: "",
            schema: [
              { name: "entity_today", required: true, selector: { entity: { domain: "sensor" } } },
              { name: "label_today", selector: { text: {} } },
              { name: "entity_tomorrow", selector: { entity: { domain: "sensor" } } },
              { name: "label_tomorrow", selector: { text: {} } },
            ],
          },
          { name: "icon", selector: { text: {} } },
          { name: "show_tomorrow", selector: { boolean: {} } },
        ],
        computeLabel: (s) =>
          ({
            title: "Titre de la carte (vide = aucun)",
            entity_today: "Entité saint du jour",
            label_today: "Libellé du jour",
            entity_tomorrow: "Entité saint de demain",
            label_tomorrow: "Libellé de demain",
            icon: "Icône / emoji",
            show_tomorrow: "Afficher le saint de demain",
          }[s.name]),
      };
    }

    static getStubConfig() {
      return { ...DEFAULTS };
    }

    setConfig(config) {
      if (!config) throw new Error("Configuration invalide");
      this._config = { ...DEFAULTS, ...config };
      this._render();
    }

    set hass(hass) {
      const c = this._config || DEFAULTS;
      const key = [c.entity_today, c.entity_tomorrow].map((e) => hass.states[e]?.state).join("|");
      this._hass = hass;
      if (key !== this._key) {
        this._key = key;
        this._render();
      }
    }

    getCardSize() {
      return this._config?.show_tomorrow === false ? 2 : 3;
    }

    _state(entity) {
      if (!entity) return null;
      const s = this._hass?.states?.[entity];
      if (!s) return { missing: true, text: `Entité introuvable : ${entity}` };
      if (["unknown", "unavailable"].includes(s.state)) return { text: "—" };
      return { text: s.state };
    }

    _row(label, st) {
      if (!st) return "";
      return `<div class="row${st.missing ? " missing" : ""}">
        <span class="icon">${esc(this._config.icon)}</span>
        <div class="txt"><div class="label">${esc(label)}</div>
        <div class="name">${esc(st.text)}</div></div></div>`;
    }

    _render() {
      if (!this._config) return;
      if (!this.shadowRoot) this.attachShadow({ mode: "open" });
      const c = this._config;
      const today = this._state(c.entity_today);
      const tomorrow = c.show_tomorrow !== false ? this._state(c.entity_tomorrow) : null;
      this.shadowRoot.innerHTML = `
        <style>
          ha-card { padding: 16px; }
          .title { font-size: 1.25em; font-weight: 500; margin-bottom: 12px; }
          .row { display: flex; align-items: center; gap: 12px; padding: 8px 0; }
          .row + .row { border-top: 1px solid var(--divider-color); }
          .icon { font-size: 1.6em; line-height: 1; }
          .label { color: var(--secondary-text-color); font-size: .85em; text-transform: uppercase; letter-spacing: .04em; }
          .name { font-size: 1.15em; font-weight: 600; }
          .missing .name { color: var(--error-color); font-weight: 400; font-size: .95em; }
        </style>
        <ha-card>
          ${c.title ? `<div class="title">${esc(c.title)}</div>` : ""}
          ${this._row(c.label_today, today)}
          ${this._row(c.label_tomorrow, tomorrow)}
        </ha-card>`;
    }
  }

  if (!customElements.get("saintdujour-card")) {
    customElements.define("saintdujour-card", SaintDuJourCard);
  }
  window.customCards = window.customCards || [];
  if (!window.customCards.some((c) => c.type === "saintdujour-card")) {
    window.customCards.push({
      type: "saintdujour-card",
      name: "Saint du jour",
      description: "Saint du jour et saint de demain (🙏), avec éditeur visuel.",
      preview: true,
    });
  }
})();
