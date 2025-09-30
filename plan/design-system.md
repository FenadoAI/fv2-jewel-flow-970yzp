# Design System - Jewellery Store Management System

## Theme Selection

**CUSTOM LUXURY JEWEL THEME**

A sophisticated design system combining the elegance of fine jewellery with professional dashboard efficiency. Inspired by luxury retail experiences with rose gold accents, deep charcoal, and pristine whites.

### Light Mode Colors:
- Background: `hsl(40, 15%, 97%)` (warm ivory)
- Card: `hsl(0, 0%, 100%)` (pure white)
- Primary: `hsl(340, 65%, 48%)` (rose gold/burgundy)
- Text: `hsl(0, 0%, 10%)` (deep charcoal)
- Muted: `hsl(40, 10%, 92%)` (soft beige)
- Border: `hsl(40, 8%, 85%)` (subtle gold-tinted gray)
- Secondary: `hsl(30, 45%, 55%)` (warm bronze)
- Accent: `hsl(280, 40%, 65%)` (amethyst purple)

### Dark Mode Colors:
- Background: `hsl(0, 0%, 8%)` (deep black)
- Card: `hsl(0, 0%, 12%)` (charcoal card)
- Primary: `hsl(340, 65%, 52%)` (brighter rose gold)
- Text: `hsl(0, 0%, 96%)` (soft white)
- Muted: `hsl(0, 0%, 16%)` (dark gray)
- Border: `hsl(0, 0%, 20%)` (subtle border)
- Secondary: `hsl(30, 45%, 60%)` (warm bronze)
- Accent: `hsl(280, 40%, 70%)` (light amethyst)

### Preview Colors:
- `hsl(340, 65%, 48%)` (rose gold)
- `hsl(30, 45%, 55%)` (bronze)
- `hsl(280, 40%, 65%)` (amethyst)

## Foundations

### Typography Scale
- **Display**: 48px/56px (hero sections, luxury product titles)
- **H1**: 36px/44px (page titles, main headings)
- **H2**: 30px/38px (section headings, category titles)
- **H3**: 24px/32px (card titles, subsections)
- **H4**: 20px/28px (component headings)
- **Body**: 16px/24px (primary content, product descriptions)
- **Small**: 14px/20px (metadata, captions, table cells)
- **Tiny**: 12px/16px (labels, badges, fine print)

**Font Families**:
- Primary: "Cormorant Garamond" (elegant serif for public catalog)
- Secondary: "Inter" (clean sans-serif for admin dashboard)
- Monospace: "JetBrains Mono" (data/SKU display)

### Spacing & Grid
- Base unit: 4px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px
- Container max-width: 1280px (admin), 1440px (catalog)
- Grid columns: 12-column responsive grid
- Gutter: 24px (mobile), 32px (desktop)

### Iconography
- Library: Lucide React
- Default size: 20px (can scale to 16px, 24px, 32px)
- Stroke width: 2px (catalog), 1.5px (dashboard)
- Key icons: Diamond (luxury), ShoppingBag, Package, Users, BarChart, Settings, Eye, Edit, Trash

## Components

### Product Card (Catalog)
**Anatomy**: Image container, title, price, quick view button, add to order button
**Variants**: Grid view (3-4 columns), List view (full width), Featured (hero size)
**States**: Default, Hover (lift shadow + scale 1.02), Out of Stock (grayscale overlay), Selected
**Styling**: White card with subtle gold border on hover, rounded corners (12px), shadow elevation on hover
**Data Slots**: productImage (aspect-ratio: 4/5), productName, price, category, stockStatus
**A11y**: Alt text for images, keyboard navigation, focus states with rose gold ring

### Inventory Data Table (Admin)
**Anatomy**: Header row, data rows, action buttons, pagination, search/filter bar
**Variants**: Compact (dense rows), Comfortable (default), Spacious (large rows)
**States**: Default, Row hover (light background), Selected row (rose gold tint), Loading skeleton
**Styling**: Striped rows (subtle), sticky header, alternating row backgrounds, 1px borders
**Data Slots**: SKU, name, category, stock quantity, price, lastUpdated, actions
**A11y**: Sortable columns (ARIA labels), keyboard navigation, screen reader announcements for updates

### Order Form
**Anatomy**: Customer info section, product selection, quantity inputs, notes textarea, submit button
**Variants**: Quick order (minimal fields), Full order (all details), Draft (save for later)
**States**: Empty, In Progress, Validating, Success, Error
**Styling**: Multi-step progress indicator, floating labels, inline validation with icons
**Data Slots**: customerName, contactInfo, selectedProducts[], quantities, specialInstructions, totalAmount
**A11y**: Required field indicators, error messages linked to inputs, keyboard shortcuts for product search

### Dashboard Widget
**Anatomy**: Title bar, content area, action menu, refresh button
**Variants**: Stat card (single metric), Chart card (graph), List card (recent items), Alert card (notifications)
**States**: Default, Loading (skeleton), Error (retry option), Empty state (illustration + CTA)
**Styling**: White card with subtle shadow, 16px padding, rose gold accent line on left edge, hover elevation
**Data Slots**: widgetTitle, metric/value, trend indicator, chart data, timestamp
**A11y**: Live regions for data updates, chart descriptions, keyboard-accessible controls

### Navigation (Role-Based)
**Anatomy**: Logo, primary nav links, user profile, theme toggle, notifications badge
**Variants**: Admin (full menu), Manager (limited options), Staff (basic access), Customer (public only)
**States**: Default, Active page (rose gold indicator), Collapsed (mobile), Expanded
**Styling**: Horizontal top bar (catalog), Vertical sidebar (admin), sticky positioning, backdrop blur
**Data Slots**: userRole, navigationItems[], notificationCount, currentPage
**A11y**: Skip to content link, ARIA current for active page, responsive mobile menu with focus trap

### Button Styles
**Primary**: Rose gold background, white text, 2px dashed border on hover, scale 0.98 on click
**Secondary**: Transparent background, rose gold border (2px solid), rose gold text, bronze border on hover
**Outline**: White background, charcoal border (1px), charcoal text, dotted border on hover
**Ghost**: No border, text only, subtle background on hover
**Icon**: Circular (40px), icon only, soft shadow, rotate 15deg on hover
**Special**: Gradient background (rose gold to bronze), white text, shimmer animation on hover

### Report Charts
**Anatomy**: Chart canvas, legend, axis labels, tooltips, export button
**Variants**: Line (trends), Bar (comparisons), Pie (distribution), Area (cumulative), Donut (categories)
**States**: Default, Loading, Interactive hover, Data point selected, No data (empty state)
**Styling**: Rose gold primary line/bar color, bronze secondary, amethyst tertiary, smooth animations
**Data Slots**: chartData[], labels[], colors[], dateRange, chartType
**A11y**: Data table alternative view, keyboard navigation between points, ARIA labels for values

## Patterns

### Product Browsing (Catalog)
**Flow**: Landing → Category filter → Product grid → Product detail → Add to order
**Components**: Hero banner, category chips, product cards grid, quick view modal, breadcrumb navigation
**A11y**: Skip links, keyboard shortcuts for filters, focus management in modals, ARIA live for filter results

### Inventory Management (Admin)
**Flow**: Dashboard → Inventory list → Edit/Add product → Save → Confirmation
**Components**: Stats overview, data table, form drawer, toast notifications, bulk action toolbar
**A11y**: Form validation, keyboard shortcuts (Ctrl+S to save), undo action, screen reader feedback

### Order Processing
**Flow**: Order form → Product search → Add items → Review → Submit → Confirmation
**Components**: Autocomplete search, order item list, running total calculator, print receipt button
**A11y**: Keyboard navigation, autocomplete with ARIA, form validation, success confirmation with sound option

## Theming

### Light Mode (Default - Catalog)
- Optimized for product photography and visual appeal
- High contrast for readability in bright environments
- Rose gold accents for luxury feel
- Warm ivory background reduces eye strain

### Dark Mode (Optional - Admin)
- Reduced eye strain for extended dashboard usage
- Maintains rose gold accents for brand consistency
- Better for low-light environments
- Chart colors adjusted for dark backgrounds

### Color Token Mapping
```
--color-luxury-primary: hsl(340, 65%, 48%)
--color-luxury-secondary: hsl(30, 45%, 55%)
--color-luxury-accent: hsl(280, 40%, 65%)
--color-success: hsl(142, 71%, 45%)
--color-warning: hsl(38, 92%, 50%)
--color-error: hsl(0, 84%, 60%)
--color-info: hsl(199, 89%, 48%)
```

## Animation & Micro-interactions

### Hover Effects
- Product cards: Lift (translateY -4px) + shadow elevation + scale 1.02 (300ms ease)
- Buttons: Dashed/dotted border animation (150ms), slight scale down on click
- Table rows: Subtle rose gold glow on left border (200ms)
- Icons: Rotate 15deg or bounce (250ms cubic-bezier)

### Transitions
- Page navigation: Fade + slide (400ms ease-out)
- Modal/drawer: Slide from right/bottom with overlay fade (350ms)
- Form validation: Shake animation for errors (400ms), checkmark bounce for success
- Data updates: Number count-up animation (600ms), chart bars grow (500ms stagger)

### Loading States
- Skeleton screens with shimmer effect (rose gold gradient)
- Spinner with rose gold accent (for quick actions)
- Progress bar with bronze-to-rose-gold gradient (for uploads)

### Unique Styling Ideas
- **Geometric Clip Paths**: Product cards with octagon/diamond-inspired corners
- **Border Treatments**: Alternating dashed/solid borders on opposite corners (e.g., top-right solid + bottom-left dashed)
- **Gradient Overlays**: Subtle radial gradient on hover (center rose gold fade)
- **3D Shadows**: Multi-layer shadows with rose gold tint for depth
- **Asymmetric Layouts**: Dashboard widgets with top-left accent corner cut
- **Animated Underlines**: Navigation links with expanding rose gold underline on hover
- **Frosted Glass**: Backdrop blur on modals and floating panels
- **Particle Effects**: Subtle sparkle animation on "Add to Order" success

## Dark Mode & Color Contrast Rules (Critical)
- Always use explicit colors - never rely on browser defaults or component variants like `variant="outline"`
- Force dark mode with CSS: `html { color-scheme: dark; }` and `meta name="color-scheme" content="dark"`
- Use high contrast ratios: minimum 4.5:1 for normal text, 3:1 for large text
- Override browser defaults with `!important` for form elements: `input, textarea, select { background-color: #000000 !important; color: #ffffff !important; }`
- Test in both light and dark system modes - system dark mode can override custom styling
- Use semantic color classes instead of component variants: `className="bg-gray-800 text-gray-300 border border-gray-600"` not `variant="outline"`
- Create CSS custom properties for consistency across components
- Quick debugging: check if using `variant="outline"`, add explicit colors, use `!important` if needed, test system modes

### Color Contrast Checklist (apply to all components):
□ No `variant="outline"` or similar browser-dependent styles
□ Explicit background and text colors specified
□ High contrast ratios (4.5:1+ for text, 3:1+ for large text)
□ Tested with system dark mode ON and OFF
□ Form elements have forced dark styling
□ Badges and buttons use custom classes, not default variants
□ Placeholder text has proper contrast
□ Focus states are visible and accessible

## Implementation Notes

### Public Catalog
- Use Cormorant Garamond for headings to convey luxury
- Large product images (minimum 800x1000px)
- Generous white space around products
- Smooth scroll behavior and lazy loading for performance

### Admin Dashboard
- Use Inter font for clarity and readability
- Dense data presentation with comfortable spacing
- Quick actions accessible via keyboard shortcuts
- Role-based component visibility using React context

### Responsive Breakpoints
- Mobile: 320-767px (single column, touch-optimized)
- Tablet: 768-1023px (2-column grid, hybrid navigation)
- Desktop: 1024px+ (full layout, hover interactions)

### Performance
- Image optimization: WebP format with fallbacks
- Lazy load below-fold content
- Code split by route (catalog vs admin)
- Cache dashboard data with stale-while-revalidate

### Accessibility Priority
- WCAG 2.1 AA compliance minimum
- Keyboard navigation for all interactive elements
- Screen reader tested with NVDA/JAWS
- Focus indicators with rose gold ring (3px, offset 2px)
- Color-blind safe palette (test with simulators)