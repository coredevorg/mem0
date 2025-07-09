# Gemini Support für OpenMemory

## Übersicht

Dieses Dokument beschreibt die Implementierung der Gemini-Unterstützung für OpenMemory MCP Server. Die Änderungen ermöglichen es, Gemini als Client in der OpenMemory UI zu verwenden.

## Durchgeführte Änderungen

### 1. Gemini Icon hinzugefügt

**Datei**: `/ui/public/images/gemini.png`
- **Quelle**: https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/google-gemini-icon.png
- **Beschreibung**: Offizielles Google Gemini Icon im PNG-Format
- **Verwendung**: Kommerziell nutzbar, keine Attribution erforderlich

### 2. Install.tsx aktualisiert

**Datei**: `/ui/components/dashboard/Install.tsx`

#### Änderung 1: clientTabs Array erweitert
```typescript
const clientTabs = [
  { key: "claude", label: "Claude", icon: "/images/claude.webp" },
  { key: "cursor", label: "Cursor", icon: "/images/cursor.png" },
  { key: "cline", label: "Cline", icon: "/images/cline.png" },
  { key: "roocline", label: "Roo Cline", icon: "/images/roocline.png" },
  { key: "windsurf", label: "Windsurf", icon: "/images/windsurf.png" },
  { key: "witsy", label: "Witsy", icon: "/images/witsy.png" },
  { key: "enconvo", label: "Enconvo", icon: "/images/enconvo.png" },
  { key: "augment", label: "Augment", icon: "/images/augment.png" },
  { key: "gemini", label: "Gemini", icon: "/images/gemini.png" }, // NEU
];
```

#### Änderung 2: colorGradientMap erweitert
```typescript
const colorGradientMap: { [key: string]: string } = {
  // ... andere Clients
  gemini: // NEU
    "data-[state=active]:bg-[linear-gradient(to_top,_rgba(66,133,244,0.3),_rgba(66,133,244,0))] data-[state=active]:border-[#4285F4]",
};
```
- **Farbe**: Google Blue (#4285F4) als Basis für Gemini-Branding

#### Änderung 3: Grid Layout angepasst
```typescript
// Vorher:
<TabsList className="... grid grid-cols-9">

// Nachher:
<TabsList className="... grid grid-cols-10">
```

### 3. source-app.tsx aktualisiert

**Datei**: `/ui/components/shared/source-app.tsx`

#### Änderung: constants Object erweitert
```typescript
export const constants = {
  // ... andere Clients
  gemini: { // NEU
    name: "Gemini",
    icon: <Icon source="/images/gemini.png" />,
    iconImage: "/images/gemini.png",
  },
  // ... default
};
```

## Installation Command

Nach den Änderungen ist folgender Installations-Command verfügbar:

```bash
npx @openmemory/install local http://localhost:8765/mcp/gemini/sse/bst --client gemini
```

## Backend-Kompatibilität

**Keine Backend-Änderungen erforderlich**: Der MCP Server unterstützt bereits dynamische Client-Namen über die Route:
```
/{client_name}/sse/{user_id}
```

## Testing

### Manuelle Tests erforderlich:

1. **UI Build testen**:
   ```bash
   make build
   make up
   ```

2. **Gemini Tab prüfen**:
   - UI auf http://localhost:3090 öffnen
   - Gemini Tab sollte in der Install-Sektion sichtbar sein
   - Korrekte Darstellung des Gemini Icons und Branding

3. **Installation Command testen**:
   ```bash
   npx @openmemory/install local http://localhost:8765/mcp/gemini/sse/bst --client gemini
   ```

4. **MCP Verbindung testen**:
   - Gemini-CLI mit OpenMemory verbinden
   - Memory-Operationen testen (add_memories, search_memory, etc.)

## Dateien geändert

| Datei | Typ | Beschreibung |
|-------|-----|-------------|
| `/ui/public/images/gemini.png` | Hinzugefügt | Gemini Icon |
| `/ui/components/dashboard/Install.tsx` | Geändert | Client-Tabs und Styling |
| `/ui/components/shared/source-app.tsx` | Geändert | Client-Konstanten |

## Aufwand

- **Geschätzt**: 15-20 Minuten
- **Tatsächlich**: ~20 Minuten
- **Komplexität**: Minimal - folgt bestehendem Pattern

## Weitere Schritte

1. Docker Image neu bauen und starten
2. UI-Tests durchführen
3. Gemini-CLI Integration testen
4. Bei Bedarf weitere Clients nach gleichem Pattern hinzufügen

## Technische Details

- **UI Framework**: Next.js mit React
- **Styling**: Tailwind CSS
- **Icons**: Statische PNG-Dateien in `/public/images/`
- **MCP Protocol**: Server-seitig bereits vollständig unterstützt

## Gemini Branding

- **Primärfarbe**: #4285F4 (Google Blue)
- **Gradient**: Transparente Overlay-Effekte für aktive Tabs
- **Icon**: Offizielles Google Gemini Logo

Die Implementierung folgt den bestehenden Design-Patterns und fügt sich nahtlos in die OpenMemory UI ein.