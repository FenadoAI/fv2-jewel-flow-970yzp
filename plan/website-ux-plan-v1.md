# Jewellery Store Management System - UX Plan v1

## Project Name and Description

**Project Name:** LuxeGems Management System

**Tagline:** "Elegance in Every Detail, Efficiency in Every Transaction"

**Description:**
LuxeGems is a comprehensive jewellery store management system that seamlessly bridges the gap between luxury retail presentation and powerful inventory management. The platform serves three distinct audiences: customers who browse an elegant public catalog and place cash-on-delivery orders; staff members who manage inventory and process orders; and managers/owners who access detailed reports and analytics. Built with a sophisticated rose gold and burgundy design language, LuxeGems combines the refinement of fine jewellery retail with the efficiency of modern business software.

The system emphasizes unique item tracking with mandatory item codes, role-based access control, and streamlined workflows that reduce friction while maintaining data integrity. Whether you're a customer browsing exquisite pieces, a staff member adding new inventory, or an owner reviewing sales performance, LuxeGems delivers an intuitive, elegant experience.

---

## Landing Page (Public Catalog)

### Hero Section

**Main Headline:** "Discover Timeless Elegance"

**Sub Headline:** "Browse our curated collection of fine jewellery, crafted with precision and delivered with care. Shop from the comfort of your home with Cash on Delivery."

**Call-to-Action Buttons:**
1. **"Explore Collection"** (Primary button - rose gold background)
   - Action: Smooth scroll to product grid section below
   - Visual: Dashed border animation on hover

2. **"Staff Login"** (Secondary button - transparent with rose gold border)
   - Action: Navigate to `/login` page
   - Visual: Positioned in top-right corner of hero, ghost button style

**Hero Image:**
Full-width background image showing luxury jewellery display (use stock image of elegant jewellery pieces on velvet background with soft lighting). Alternatively, use AI-generated abstract geometric pattern with rose gold and burgundy gradient overlay.

### Logo
**Generate logo using AI:**
"Create a sleek and modern abstract logo for a luxury jewellery startup named "LuxeGems", using only minimalist geometric shapes and a rose gold and deep burgundy color scheme. Do not include any typography. The design should convey elegance, sophistication, and timeless luxury purely through abstract visual elements, suitable for both digital and print media. No typography."

Use this logo as favicon and in the navigation header.

### Demo Section (For Free Users)
Not applicable for this project - customers can browse the full catalog without registration.

### Features Section

**Section Title:** "Why Choose LuxeGems"

**Feature 1: Curated Collection**
- Icon: Diamond icon (Lucide)
- Title: "Handpicked Excellence"
- Description: "Every piece in our collection is carefully selected for quality, craftsmanship, and timeless appeal. From classic designs to contemporary statements."

**Feature 2: Easy Ordering**
- Icon: ShoppingBag icon (Lucide)
- Title: "Simple Cash on Delivery"
- Description: "Browse, select, and order with confidence. Pay only when your jewellery arrives at your doorstep. No online payment hassles."

**Feature 3: Detailed Information**
- Icon: Eye icon (Lucide)
- Title: "Complete Transparency"
- Description: "View detailed specifications including weight, material, pricing, and high-resolution images. Know exactly what you're ordering."

**Feature 4: Fast Processing**
- Icon: Package icon (Lucide)
- Title: "Quick Delivery"
- Description: "Orders processed by our expert team within 24 hours. Track your order status from confirmation to delivery."

**Layout:** 4-column grid on desktop, 2-column on tablet, single column on mobile. Each feature in a white card with subtle rose gold border on hover.

### Product Grid Section

**Section Title:** "Our Collection"

**Filter Bar:**
- Category chips: All, Rings, Necklaces, Bracelets, Earrings, Pendants
- Material dropdown: All Materials, Gold, Silver, Diamond, Platinum, Ruby, Emerald
- Search bar: "Search by name or item code..."
- Sort dropdown: Featured, Price: Low to High, Price: High to Low, Newest First

**Product Card Design:**
- Image: 4:5 aspect ratio (portrait orientation)
- Item name: H4 typography (Cormorant Garamond)
- Item code: Small text (monospace font, muted color)
- Material: Badge with bronze accent
- Price: Large, prominent (rose gold color)
- Status badge: "Available" (green), "Reserved" (amber), "Sold" (gray)
- Quick view button: Eye icon (appears on hover)
- "View Details" button: Secondary style

**Grid Layout:** 4 columns on desktop, 3 on tablet, 2 on mobile with 24px gaps

**Interaction:**
- Hover: Card lifts with shadow elevation, scales to 1.02
- Click product card: Navigate to item detail page
- Click quick view: Open modal with larger image and basic info

**Images to Include:**
- Stock images of various jewellery pieces (rings, necklaces, bracelets)
- Each product card should have 1 hero image
- Use high-quality stock photos from luxury jewellery collections

### Testimonials Section

**Section Title:** "What Our Customers Say"

**Testimonial 1:**
- Quote: "The quality exceeded my expectations. The online catalog made it so easy to browse, and the COD option gave me confidence. My diamond ring is absolutely stunning!"
- Author: "Priya Sharma"
- Location: "Mumbai"
- Rating: 5 stars (rose gold star icons)

**Testimonial 2:**
- Quote: "Professional service from start to finish. The detailed product specifications helped me choose the perfect anniversary gift. Highly recommended!"
- Author: "Rajesh Kumar"
- Location: "Delhi"
- Rating: 5 stars

**Testimonial 3:**
- Quote: "Beautiful collection and transparent pricing. The staff was helpful when I called to confirm details. My necklace arrived exactly as shown in the photos."
- Author: "Anita Desai"
- Location: "Bangalore"
- Rating: 5 stars

**Layout:** 3-column carousel on desktop, single card carousel on mobile. Each testimonial in a white card with amethyst left border accent.

### CTA Section

**Background:** Soft gradient (rose gold to bronze) with subtle geometric pattern overlay

**Headline:** "Ready to Find Your Perfect Piece?"

**Sub-text:** "Explore our collection and place your order today. Free consultation available for custom requests."

**CTA Button:** "Browse Collection" (white background, rose gold text)
- Action: Scroll back to product grid

**Secondary CTA:** "Contact Us" (transparent with white border)
- Action: Open contact dialog/modal with phone number, email, and business hours

### Footer

**Layout:** 3-column layout on desktop, single column stacked on mobile

**Column 1: Brand**
- LuxeGems logo
- Tagline: "Elegance in Every Detail"
- Brief description: "Your trusted destination for fine jewellery with transparent pricing and reliable delivery."

**Column 2: Quick Links**
- Browse Collection (link to catalog section)
- About Us (link to about section on same page)
- Contact Us (opens contact modal)
- Staff Login (link to /login)

**Column 3: Contact Information**
- Phone: +91 98765 43210
- Email: info@luxegems.com
- Business Hours: Mon-Sat, 10 AM - 7 PM
- Address: (Add placeholder address)

**Column 4: Social Media**
- Instagram icon (link to Instagram)
- Facebook icon (link to Facebook)
- WhatsApp icon (link to WhatsApp business)

**Bottom Bar:**
- Copyright: "© 2024 LuxeGems. All rights reserved."
- Built with love for jewellery enthusiasts

**Footer Background:** Deep charcoal (dark mode colors) with rose gold accents

**Images/Icons:** Use Lucide icons for social media, phone, email. Keep footer minimal and elegant.

---

## Item Detail Page

**Route:** `/item/{id}`

**Layout:** 2-column layout on desktop (image gallery left, details right), stacked on mobile

### Left Column: Image Gallery

**Main Image Display:**
- Large image viewer (800x1000px minimum)
- Zoom on hover functionality
- Click to open fullscreen lightbox
- Background: Soft ivory (matches landing page)

**Thumbnail Gallery:**
- Horizontal row of thumbnails below main image
- 4-5 thumbnails visible, scroll for more
- Active thumbnail highlighted with rose gold border
- Click thumbnail to change main image

**Image Placeholder:**
If no images available, show elegant placeholder with diamond icon and text "Image coming soon"

### Right Column: Product Details

**Breadcrumb Navigation:**
Home > Collection > {Category} > {Item Name}

**Item Name:** H1 typography (Cormorant Garamond, 36px)

**Item Code:** Small text with monospace font, copy-to-clipboard icon
- Format: "SKU: {item_code}" with copy icon
- Click to copy: Show toast "Item code copied!"

**Price:** Large display (H2, rose gold color)
- Format: "₹ {price}"
- Note: Prices stored in cents in backend, display as rupees with proper conversion

**Status Badge:**
- Available: Green background, white text
- Reserved: Amber background, white text
- Sold: Gray background, white text

**Specifications Table:**
- Material: {material}
- Weight: {weight}g
- Category: {category}
- Added: {created_at} (format: "12 Jan 2024")
- Last Updated: {updated_at}

**Description:**
- Body text (16px/24px)
- Markdown support for formatting
- Collapsible if text is very long (show "Read more" after 3 lines)

**Action Buttons:**

1. **"Add to Order"** (Primary button, full width)
   - Action: Opens order placement dialog (see Popups section)
   - Disabled if status is "Sold"
   - Shows "Out of Stock" if not available

2. **"Back to Collection"** (Secondary button, full width)
   - Action: Navigate back to landing page catalog

**Related Items Section:** (Below main content)
- "You May Also Like"
- Show 4 similar items (same category or material)
- Product cards matching landing page design

**Images Needed:**
- Multiple high-quality product photos from different angles
- Detail shots showing craftsmanship
- Lifestyle images showing jewellery being worn

---

## Login/Dashboard Page

### Login Page

**Route:** `/login`

**Layout:** Centered card (max-width 400px) on full-screen background

**Background:** Subtle geometric pattern with rose gold gradient overlay, or luxury jewellery image with dark overlay

**Login Card:**

**Logo:** LuxeGems logo at top center

**Heading:** "Welcome Back" (H2, center aligned)

**Form Fields:**
1. Email/Username input
   - Label: "Email"
   - Placeholder: "Enter your email"
   - Type: email
   - Validation: Required, valid email format

2. Password input
   - Label: "Password"
   - Placeholder: "Enter your password"
   - Type: password (with show/hide toggle icon)
   - Validation: Required, minimum 6 characters

**Login Button:** "Sign In" (Primary button, full width)
- Action: POST /api/auth/login
- On success: Navigate to dashboard based on role
- On error: Show error message below button in red

**Error Message Display:**
- "Invalid credentials. Please try again."
- Red text with error icon
- Positioned below login button

**Footer Link:**
- "Forgot Password?" (ghost button, center aligned)
- Note: For MVP, can show toast "Please contact admin"

**Back to Catalog Link:**
- "← Back to Catalog" (top-left corner, ghost button)
- Action: Navigate to landing page

### Dashboard Page (All Roles)

**Route:** `/dashboard`

**Layout:** Sidebar navigation (left) + main content area (right)

**Sidebar Navigation:**

**Logo:** LuxeGems logo at top

**User Profile Section:**
- User avatar (initials in circle with rose gold background)
- Username
- Role badge (Staff/Manager/Owner with appropriate colors)
- Logout button (ghost style)

**Navigation Menu:**

**For Staff:**
- Dashboard (BarChart icon) - `/dashboard`
- Inventory (Package icon) - `/dashboard/inventory`
- Orders (ShoppingBag icon) - `/dashboard/orders`

**For Manager (adds to staff menu):**
- Reports (TrendingUp icon) - `/dashboard/reports`

**For Owner (adds to manager menu):**
- Users (Users icon) - `/dashboard/users`

**Active Page Indicator:** Rose gold left border (4px) and background tint

**Bottom Section:**
- Theme toggle (Sun/Moon icon)
- Settings (Settings icon) - opens settings dialog

### Dashboard Home (Overview)

**Page Title:** "Dashboard Overview"

**Date Range Selector:** (Top right)
- Last 7 Days / Last 30 Days / Last 90 Days / Custom
- Default: Last 30 Days

**Stats Cards Row (4 columns):**

**Card 1: Total Inventory**
- Large number: Total items count
- Icon: Package (rose gold)
- Trend indicator: "+12 this month" (green if positive, red if negative)
- Visual: Mini bar chart showing weekly trend

**Card 2: Available Items**
- Large number: Available items count
- Icon: Diamond
- Percentage: "X% of total inventory"
- Visual: Donut chart showing available vs sold vs reserved

**Card 3: Pending Orders**
- Large number: Orders with "pending" status
- Icon: ShoppingBag (amber color)
- Subtitle: "Requires attention"
- Action button: "View Orders" (navigate to orders page)

**Card 4: Total Revenue** (Manager/Owner only)
- Large number: Revenue in rupees (from date range)
- Icon: TrendingUp (green)
- Trend: "+X% from last period"
- Visual: Line chart showing daily revenue

**Recent Activity Section:**

**Left Column (66% width): Recent Orders**
- Section title: "Recent Orders"
- Table with columns: Order ID, Customer, Items, Amount, Status, Date
- Show 5 most recent orders
- Status badges with color coding
- Action: Click row to view order details
- "View All Orders" button at bottom

**Right Column (33% width): Quick Actions**
- "Add New Item" button (Primary)
  - Action: Opens add item dialog
- "View Inventory" button (Secondary)
  - Action: Navigate to inventory page
- "Low Stock Alert" widget
  - Show count of items with low stock (future enhancement placeholder)
  - Bronze color badge

**Low Stock Items Widget:** (Manager/Owner only)
- Section title: "Low Stock Alert"
- List of items below threshold (placeholder for future)
- For MVP: Show message "Coming soon: Automated stock alerts"

**Images/Visuals:**
- Small chart visualizations in stat cards
- Icons from Lucide library
- Empty state illustrations if no recent activity

---

## Inventory Management Page

**Route:** `/dashboard/inventory`

**Page Title:** "Inventory Management"

**Page Header:**
- Title on left
- "Add New Item" button on right (Primary, with Plus icon)
  - Action: Opens add item dialog

**Filter & Search Bar:**

**Search Input:** (Left side, 40% width)
- Placeholder: "Search by name, item code, or material..."
- Search icon on left
- Clear button (X icon) on right when text entered
- Real-time search as user types (debounced 300ms)

**Filter Dropdowns:** (Right side)
1. Category filter: All Categories / Rings / Necklaces / Bracelets / Earrings
2. Material filter: All Materials / Gold / Silver / Diamond / Platinum
3. Status filter: All Status / Available / Sold / Reserved

**Results Counter:**
- "Showing X of Y items" (below filters, left aligned)

**Data Table:**

**Columns:**
1. **Image** (60px thumbnail)
   - Square thumbnail with rounded corners
   - Placeholder if no image

2. **Item Code** (100px)
   - Monospace font
   - Copy icon on hover
   - Sortable

3. **Name** (200px)
   - Primary text
   - Truncate with ellipsis if too long
   - Sortable

4. **Category** (120px)
   - Badge style with category color
   - Sortable

5. **Material** (120px)
   - Regular text
   - Sortable

6. **Weight** (80px)
   - Format: "X.Xg"
   - Right aligned
   - Sortable

7. **Price** (100px)
   - Format: "₹ X,XXX"
   - Right aligned
   - Bold text
   - Sortable (default sort: high to low)

8. **Status** (100px)
   - Badge with color coding
   - Available (green), Sold (gray), Reserved (amber)
   - Filterable

9. **Updated** (100px)
   - Relative time: "2 days ago"
   - Tooltip shows full date on hover
   - Sortable (default: newest first)

10. **Actions** (80px)
    - Edit icon button (opens edit dialog)
    - Eye icon button (navigate to item detail page)

**Table Features:**
- Sticky header row (stays visible on scroll)
- Alternating row background colors (subtle)
- Hover state: Row highlights with rose gold tint on left border
- Click row: Navigate to item detail page (except when clicking action buttons)
- Checkbox column for bulk actions (future enhancement, placeholder for MVP)

**Pagination:**
- Bottom of table, center aligned
- Previous / Page numbers / Next buttons
- "Items per page" dropdown: 20 / 50 / 100
- Current page highlighted with rose gold

**Empty State:**
- Illustration: Diamond icon with message
- Text: "No items found"
- Sub-text: "Try adjusting your filters or add a new item"
- "Add New Item" button

**Loading State:**
- Skeleton rows with shimmer effect (rose gold gradient)

---

## Order Management Page

**Route:** `/dashboard/orders`

**Page Title:** "Order Management"

**Status Filter Tabs:** (Below title)
- All Orders (count badge)
- Pending (amber badge)
- Confirmed (blue badge)
- Delivered (green badge)
- Cancelled (red badge)

**Search & Filter Bar:**

**Search Input:** (Left side)
- Placeholder: "Search by customer name, phone, or order ID..."
- Search icon

**Date Range Picker:** (Right side)
- Quick filters: Today / Last 7 Days / Last 30 Days / Custom
- Custom shows calendar popup

**Results Counter:**
- "Showing X orders" (below tabs)

**Orders Table:**

**Columns:**

1. **Order ID** (120px)
   - Format: "#ORD-XXXXX" (shortened UUID)
   - Monospace font
   - Copy icon on hover
   - Click to view full details

2. **Customer Name** (150px)
   - Primary text, bold
   - Phone number below in smaller text

3. **Items** (80px)
   - Count: "3 items"
   - Tooltip on hover shows item names

4. **Total Amount** (100px)
   - Format: "₹ X,XXX"
   - Right aligned, bold
   - Rose gold color

5. **Status** (100px)
   - Badge with color coding
   - Pending (amber), Confirmed (blue), Delivered (green), Cancelled (red)

6. **Payment** (80px)
   - "COD" badge (all orders)
   - Bronze color

7. **Order Date** (120px)
   - Format: "12 Jan 2024, 3:45 PM"
   - Sortable (default: newest first)

8. **Actions** (120px)
   - Status update dropdown button
   - Eye icon (view details)
   - Print icon (print receipt) - future enhancement

**Status Update Dropdown:**
- Shows current status and available transitions
- Example: Pending → can change to Confirmed or Cancelled
- Confirmed → can change to Delivered or Cancelled
- Delivered → no changes allowed
- Cancelled → no changes allowed

**Click Row Action:**
- Opens order detail dialog/drawer (see Popups section)

**Empty State:**
- Illustration: Shopping bag icon
- Text: "No orders found"
- Sub-text: "Orders will appear here once customers place them"

**Order Detail Dialog Contents:**
- Customer information section
- Delivery address
- Order items table (item name, code, quantity, price, subtotal)
- Total amount calculation
- Order timeline (status changes with timestamps)
- Action buttons: Update Status / Print Receipt / Close

---

## Reports Page (Manager/Owner Only)

**Route:** `/dashboard/reports`

**Access Control:**
- Redirect to dashboard if user role is "staff"
- Show 403 error page if accessed directly

**Page Title:** "Reports & Analytics"

**Tab Navigation:**
- Inventory Report
- Sales Report

### Inventory Report Tab

**Date Range:** Not applicable (shows current inventory snapshot)

**Filter Options:**
- Category dropdown: All / Rings / Necklaces / Bracelets / Earrings
- Material dropdown: All / Gold / Silver / Diamond / Platinum

**Summary Cards (4 columns):**

**Card 1: Total Items**
- Large number: Total inventory count
- Icon: Package
- Breakdown: Available / Sold / Reserved counts

**Card 2: Total Value**
- Large number: Sum of all item prices (in rupees)
- Icon: Coins
- Breakdown: Value by status

**Card 3: Available Items**
- Large number: Available count
- Percentage of total
- Green indicator

**Card 4: Sold Items**
- Large number: Sold count
- Percentage of total
- Gray indicator

**Charts Section:**

**Chart 1: Inventory by Category (Pie Chart)**
- Shows distribution of items across categories
- Color coded segments (rose gold, bronze, amethyst, etc.)
- Hover shows count and percentage
- Legend on right side

**Chart 2: Inventory by Material (Bar Chart)**
- X-axis: Material types
- Y-axis: Item count
- Bars colored in rose gold gradient
- Hover shows exact count

**Chart 3: Inventory Value Distribution (Donut Chart)**
- Shows value distribution by category
- Center shows total value
- Color coded segments

**Detailed Breakdown Table:**
- Category | Total Items | Available | Sold | Reserved | Total Value
- Sortable by any column
- Footer row shows totals

**Export Button:**
- "Export Report" (Secondary button, top right)
- Action: Downloads CSV (future enhancement, show toast "Coming soon")

### Sales Report Tab

**Date Range Selector:** (Top section)
- Start date and end date pickers
- Quick filters: Last 7 Days / Last 30 Days / Last 90 Days / This Year
- "Apply" button to refresh data

**Summary Cards (4 columns):**

**Card 1: Total Orders**
- Large number: Order count
- Icon: ShoppingBag
- Breakdown: By status (pending, confirmed, delivered, cancelled)

**Card 2: Completed Orders**
- Large number: Delivered orders count
- Percentage of total orders
- Green indicator

**Card 3: Total Revenue**
- Large number: Sum of all completed orders (in rupees)
- Icon: TrendingUp
- Comparison: "+X% from previous period"

**Card 4: Pending Orders**
- Large number: Pending orders count
- Amber indicator
- Action: "View Pending" button

**Charts Section:**

**Chart 1: Sales Trend (Line Chart)**
- X-axis: Date (daily, weekly, or monthly based on range)
- Y-axis: Revenue in rupees
- Rose gold line with gradient fill below
- Hover shows exact amount and date

**Chart 2: Orders by Status (Bar Chart)**
- X-axis: Status types
- Y-axis: Order count
- Color coded bars

**Chart 3: Revenue Breakdown (Area Chart)**
- Shows cumulative revenue over time
- Multiple areas for different categories (if available)
- Stacked or overlaid based on data

**Top Selling Items Table:**
- Columns: Item Code | Item Name | Quantity Sold | Total Revenue
- Shows top 10 items
- Sortable by quantity or revenue
- Click item to navigate to item detail

**Export Button:**
- "Export Sales Report" (Secondary button)
- Action: Downloads CSV with detailed sales data (future, show toast "Coming soon")

**Empty State (No Sales in Date Range):**
- Illustration: Empty chart icon
- Text: "No sales data available for selected period"
- Sub-text: "Try selecting a different date range"

---

## User Management Page (Owner Only)

**Route:** `/dashboard/users`

**Access Control:**
- Only accessible to users with "owner" role
- Redirect to dashboard for manager/staff

**Page Title:** "User Management"

**Page Header:**
- Title on left
- "Add New User" button on right (Primary, with UserPlus icon)
  - Action: Opens add user dialog

**Filter Bar:**
- Role filter: All Roles / Staff / Manager / Owner
- Search: "Search by name, email, or username..."

**Users Table:**

**Columns:**

1. **Avatar** (60px)
   - Circle with user initials
   - Background color based on role (staff: blue, manager: green, owner: rose gold)

2. **Username** (150px)
   - Primary text, bold
   - Email below in smaller text

3. **Email** (200px)
   - Regular text
   - Clickable mailto link

4. **Role** (100px)
   - Badge with role-specific color
   - Staff (blue), Manager (green), Owner (rose gold)

5. **Created** (120px)
   - Format: "12 Jan 2024"
   - Relative time in tooltip: "3 months ago"

6. **Status** (80px)
   - Active (green badge) / Inactive (gray badge)
   - For MVP, all users are active

7. **Actions** (100px)
   - Edit icon button (opens edit user dialog)
   - Trash icon button (opens delete confirmation)
   - Disabled for current user (can't delete self)

**User Actions:**
- Edit: Opens dialog to change username, email, role, password
- Delete: Shows confirmation dialog
  - "Are you sure you want to delete {username}?"
  - "This action cannot be undone."
  - Cancel / Delete buttons

**Empty State:**
- Illustration: Users icon
- Text: "No users found"
- "Add New User" button

**Note for MVP:**
- User management endpoints are not in the API contract
- Show placeholder message: "User management is coming soon. Please contact system administrator to add/modify users."
- Table can display existing users fetched via GET /auth/me or hardcoded sample data
- Add/Edit/Delete functionality will be enabled in future phase

---

## Popups/Dialogs

### 1. Order Placement Dialog

**Trigger:** Clicking "Add to Order" on item detail page

**Dialog Title:** "Place Order"

**Dialog Size:** Medium (600px width)

**Content:**

**Section 1: Selected Item (Read-only)**
- Small product image (80px thumbnail)
- Item name
- Item code
- Price per unit
- Quantity selector (default: 1, min: 1, max: 10)
  - Minus/Plus buttons with number input
  - Total price updates automatically

**Section 2: Customer Information**

**Form Fields:**

1. **Customer Name** (required)
   - Label: "Full Name"
   - Placeholder: "Enter your full name"
   - Validation: Min 2 characters, max 100 characters

2. **Phone Number** (required)
   - Label: "Contact Number"
   - Placeholder: "+91 98765 43210"
   - Validation: Valid phone format
   - Helper text: "We'll call to confirm your order"

3. **Delivery Address** (required)
   - Label: "Complete Delivery Address"
   - Textarea (4 rows)
   - Placeholder: "House/Flat No., Building, Street, Landmark, City, Pincode"
   - Validation: Min 10 characters
   - Character counter: "X/500"

4. **Special Instructions** (optional)
   - Label: "Special Instructions (Optional)"
   - Textarea (2 rows)
   - Placeholder: "Any specific delivery instructions?"

**Section 3: Order Summary**

- Subtotal: ₹ X,XXX (item price × quantity)
- Delivery: FREE (green text)
- Total Amount: ₹ X,XXX (bold, large, rose gold color)
- Payment Method: "Cash on Delivery (COD)" (badge)

**Action Buttons:**

1. **"Place Order"** (Primary button, full width)
   - Action: POST /api/orders
   - Shows loading spinner during API call
   - On success: Show success message and close dialog
   - On error: Show error message inline

2. **"Cancel"** (Secondary button, full width)
   - Action: Close dialog without saving

**Success State:**
- Replace dialog content with success message
- Icon: Checkmark with animation
- Message: "Order Placed Successfully!"
- Sub-text: "Order ID: #ORD-XXXXX"
- Details: "We'll contact you shortly to confirm delivery details."
- Button: "Continue Shopping" (navigate back to catalog)

**Error State:**
- Show error message in red banner at top of dialog
- Example errors:
  - "Item no longer available"
  - "Please fill all required fields"
  - "Phone number format invalid"

### 2. Add/Edit Inventory Item Dialog

**Trigger:**
- Clicking "Add New Item" button on inventory page (add mode)
- Clicking edit icon on inventory table row (edit mode)

**Dialog Title:**
- Add mode: "Add New Item"
- Edit mode: "Edit Item: {item_code}"

**Dialog Size:** Large (800px width)

**Content:**

**Image Upload Section:**
- Drag-and-drop zone or click to upload
- Multiple images supported (up to 5)
- Preview thumbnails below upload zone
- Remove button (X) on each thumbnail
- Note: "For MVP, paste image URLs directly"
- Text input field for image URLs (comma-separated)

**Form Fields (2-column layout):**

**Left Column:**

1. **Item Code** (required, unique)
   - Label: "Item Code (SKU)"
   - Placeholder: "e.g., RNG-001"
   - Validation: Alphanumeric, max 50 characters, must be unique
   - Helper text: "Unique identifier for this item"
   - Disabled in edit mode (cannot change item code)

2. **Item Name** (required)
   - Label: "Item Name"
   - Placeholder: "e.g., Diamond Solitaire Ring"
   - Validation: Min 3 chars, max 200 chars

3. **Category** (required)
   - Label: "Category"
   - Dropdown: Ring / Necklace / Bracelet / Earring / Pendant / Other
   - Searchable dropdown

4. **Material** (required)
   - Label: "Material"
   - Dropdown: Gold / Silver / Diamond / Platinum / Ruby / Emerald / Sapphire / Other
   - Or free text input with autocomplete

**Right Column:**

5. **Price** (required)
   - Label: "Price (₹)"
   - Number input
   - Placeholder: "10000"
   - Validation: Integer >= 0
   - Helper text: "Enter price in rupees (will be stored in cents)"

6. **Weight** (required)
   - Label: "Weight (grams)"
   - Number input (decimal allowed)
   - Placeholder: "15.5"
   - Validation: Float > 0

7. **Status** (required)
   - Label: "Status"
   - Radio buttons: Available / Reserved / Sold
   - Default: Available

**Full Width:**

8. **Description** (required)
   - Label: "Description"
   - Textarea (6 rows)
   - Placeholder: "Detailed description of the item, including design details, craftsmanship, occasion, etc."
   - Validation: Min 10 characters
   - Character counter: "X/1000"
   - Markdown support hint

**Action Buttons:**

1. **"Save Item"** (Primary button)
   - Add mode: POST /api/inventory/items
   - Edit mode: PATCH /api/inventory/items/{id}
   - Shows loading spinner during API call
   - On success: Close dialog, refresh inventory table, show success toast
   - On error: Show error message inline (e.g., "Item code already exists")

2. **"Cancel"** (Secondary button)
   - Action: Close dialog without saving
   - Show confirmation if form has unsaved changes: "Discard changes?"

**Validation:**
- Real-time validation on blur
- Show error messages below each field
- Disable "Save Item" button until all required fields are valid

### 3. Order Detail Drawer

**Trigger:** Clicking on order row in orders table

**Layout:** Slide-in drawer from right side (500px width)

**Header:**
- Title: "Order Details"
- Close button (X icon, top right)

**Content:**

**Order ID Section:**
- Large order ID: "#ORD-XXXXX"
- Copy icon to copy full UUID
- Status badge (large, prominent)

**Customer Information Card:**
- Icon: User icon
- Name: {customer_name}
- Phone: {customer_phone} (clickable tel: link)
- Address: {customer_address} (formatted with line breaks)

**Order Items Section:**
- Title: "Ordered Items"
- Table with columns: Item, Quantity, Price, Subtotal
- Each row shows:
  - Small thumbnail image (40px)
  - Item name and code
  - Quantity as badge
  - Price per unit
  - Subtotal (quantity × price)
- Footer row: Total Amount (bold, rose gold)

**Payment Information:**
- Payment Method: "Cash on Delivery" badge
- Amount: ₹ X,XXX (large, rose gold)

**Order Timeline:**
- Vertical timeline showing status history
- Each status change with:
  - Status name
  - Timestamp
  - Icon (checkmark for completed steps)
- Visual: Connected dots with lines, completed steps in rose gold

**Delivery Information:**
- Order Date: {order_date}
- Delivery Date: {delivery_date} (if delivered, else "Pending")
- Expected Delivery: "Within 3-5 business days" (if not delivered)

**Action Buttons:**

1. **"Update Status"** (Primary button)
   - Opens inline status update form
   - Dropdown to select new status
   - Date picker for delivery date (if changing to "delivered")
   - Save button: PATCH /api/orders/{id}/status
   - Cancel button to close form

2. **"Print Receipt"** (Secondary button, icon)
   - Action: Opens print-friendly view in new tab (future enhancement)
   - For MVP: Show toast "Coming soon"

3. **"Close"** (Ghost button)
   - Action: Close drawer

**Status Update Form (inline):**
- Appears when "Update Status" is clicked
- Current status shown (read-only)
- New status dropdown (only valid transitions)
- Delivery date picker (if changing to "delivered")
- Notes textarea (optional, for internal use - future enhancement)
- Save / Cancel buttons

### 4. Contact Us Dialog

**Trigger:** Clicking "Contact Us" button in footer or CTA section

**Dialog Title:** "Get in Touch"

**Dialog Size:** Medium (500px width)

**Content:**

**Contact Information:**

1. **Phone**
   - Icon: Phone icon
   - Number: +91 98765 43210
   - Clickable tel: link
   - Helper text: "Call us Mon-Sat, 10 AM - 7 PM"

2. **Email**
   - Icon: Mail icon
   - Email: info@luxegems.com
   - Clickable mailto: link
   - Helper text: "We respond within 24 hours"

3. **WhatsApp**
   - Icon: WhatsApp icon (green)
   - Button: "Chat on WhatsApp"
   - Action: Opens WhatsApp web/app with pre-filled message
   - Message template: "Hi, I'm interested in your jewellery collection..."

4. **Visit Us**
   - Icon: MapPin icon
   - Address: (placeholder address)
   - "Get Directions" link (opens Google Maps)

**Business Hours:**
- Monday - Saturday: 10:00 AM - 7:00 PM
- Sunday: Closed
- Public Holidays: Closed

**Social Media Links:**
- Instagram, Facebook icons with links
- "Follow us for latest collections" text

**Close Button:**
- "Close" button at bottom (Secondary style)

### 5. Delete Confirmation Dialog

**Trigger:** Clicking delete icon on user management table (owner only)

**Dialog Title:** "Confirm Deletion"

**Dialog Size:** Small (400px width)

**Content:**

**Warning Icon:** Red triangle with exclamation mark

**Message:**
- "Are you sure you want to delete user {username}?"
- "This action cannot be undone."

**User Details:**
- Username: {username}
- Email: {email}
- Role: {role}

**Action Buttons:**

1. **"Delete User"** (Destructive button, red background)
   - Action: DELETE /api/users/{id} (when endpoint available)
   - Shows loading spinner
   - On success: Close dialog, refresh users table, show success toast
   - On error: Show error message

2. **"Cancel"** (Secondary button)
   - Action: Close dialog without deleting

---

## User Flows

### User Flow 1: Customer Browsing and Ordering

**Goal:** Customer discovers jewellery and places a COD order

**Steps:**

1. **Landing:** Customer arrives at landing page (homepage)
   - Views hero section with main headline and CTA
   - Sees featured images and branding

2. **Browse Collection:** Customer scrolls down or clicks "Explore Collection"
   - Views product grid with category filters visible
   - Sees product cards with images, names, prices

3. **Filter & Search:** Customer applies filters
   - Clicks category chip (e.g., "Necklaces")
   - Optionally selects material filter (e.g., "Gold")
   - Product grid updates to show matching items
   - Result count updates: "Showing 12 of 45 items"

4. **View Product:** Customer clicks on a product card
   - Navigates to item detail page
   - Views large product images (can click to zoom)
   - Reads description, specifications
   - Sees price prominently displayed
   - Checks status badge: "Available"

5. **Place Order:** Customer clicks "Add to Order" button
   - Order placement dialog opens
   - Item details pre-filled with quantity selector
   - Customer fills form:
     * Name: "Anita Sharma"
     * Phone: "+91 98765 43210"
     * Address: "123, MG Road, Koramangala, Bangalore - 560034"
     * Special instructions: "Please call before delivery"

6. **Review & Submit:** Customer reviews order summary
   - Checks total amount
   - Sees payment method: "COD"
   - Clicks "Place Order" button

7. **Confirmation:** Success message appears
   - "Order Placed Successfully!"
   - Order ID displayed: "#ORD-12345"
   - Message: "We'll contact you shortly to confirm delivery details."
   - Customer clicks "Continue Shopping"

8. **Return to Catalog:** Customer returns to landing page
   - Can browse more items or leave site

**Success Criteria:**
- Order created in database with "pending" status
- Customer information captured correctly
- Item status unchanged (still "available" for jewellery)
- Customer sees confirmation message

**Alternate Flows:**
- If item becomes unavailable during order: Show error "Item no longer available"
- If validation fails: Show field-specific error messages, prevent submission
- Customer can cancel order dialog at any time

---

### User Flow 2: Staff Adding Inventory and Processing Orders

**Goal:** Staff member adds new jewellery items and updates order status

**Steps:**

1. **Login:** Staff navigates to login page
   - Enters email: "staff@luxegems.com"
   - Enters password: "********"
   - Clicks "Sign In"
   - System validates credentials via POST /api/auth/login

2. **Dashboard Landing:** Staff redirected to dashboard home
   - Sees dashboard overview with stats
   - Views recent orders in activity section
   - Sidebar navigation visible with available menu items

3. **Navigate to Inventory:** Staff clicks "Inventory" in sidebar
   - Navigates to `/dashboard/inventory`
   - Sees inventory table with all items
   - Filters and search bar visible at top

4. **Add New Item:** Staff clicks "Add New Item" button
   - Add inventory dialog opens
   - Staff fills form:
     * Item Code: "RNG-042" (unique)
     * Name: "Sapphire Engagement Ring"
     * Category: "Ring" (dropdown)
     * Material: "Platinum" (dropdown)
     * Price: "150000" (rupees)
     * Weight: "12.5" (grams)
     * Status: "Available" (radio button)
     * Description: "Exquisite platinum ring featuring a 2-carat oval sapphire..."
     * Images: (pastes image URLs)

5. **Save Item:** Staff reviews and clicks "Save Item"
   - System validates all fields
   - POST /api/inventory/items
   - Success toast appears: "Item added successfully"
   - Dialog closes
   - Inventory table refreshes with new item at top

6. **Navigate to Orders:** Staff clicks "Orders" in sidebar
   - Navigates to `/dashboard/orders`
   - Sees orders table with all orders
   - "Pending" tab shows 3 orders

7. **View Order Details:** Staff clicks on pending order row
   - Order detail drawer slides in from right
   - Staff reviews:
     * Customer: "Anita Sharma"
     * Phone: "+91 98765 43210"
     * Items: 1 item - "Diamond Necklace"
     * Total: "₹ 85,000"
     * Status: "Pending"
     * Order Date: "28 Jan 2024, 2:30 PM"

8. **Update Order Status:** Staff clicks "Update Status"
   - Inline status update form appears
   - Staff selects new status: "Confirmed" from dropdown
   - Clicks "Save"
   - PATCH /api/orders/{id}/status
   - Success toast: "Order status updated"
   - Timeline updates with new status entry
   - Status badge changes to "Confirmed" (blue)

9. **Process Next Order:** Staff closes drawer
   - Returns to orders table
   - "Pending" count decreased by 1
   - Can process next order or view other tabs

10. **Logout:** Staff clicks user profile in sidebar
    - Clicks "Logout" button
    - Redirected to login page
    - JWT token cleared

**Success Criteria:**
- New item visible in inventory with correct details
- Order status updated in database
- Staff can seamlessly switch between inventory and orders
- All changes reflected in real-time

**Alternate Flows:**
- If item code already exists: Show error "Item code already exists"
- If order status transition is invalid: Show error (though UI should prevent this)
- Staff can edit existing items by clicking edit icon
- Staff can search/filter inventory before adding

---

### User Flow 3: Manager Viewing Reports

**Goal:** Manager accesses inventory and sales reports to analyze business performance

**Steps:**

1. **Login:** Manager navigates to login page
   - Enters credentials (email: "manager@luxegems.com")
   - Clicks "Sign In"
   - System authenticates and identifies role as "manager"

2. **Dashboard Landing:** Manager redirected to dashboard
   - Sees expanded stats including revenue card (visible to manager+)
   - Views "Total Revenue" card with trend indicator
   - Dashboard shows last 30 days by default

3. **Navigate to Reports:** Manager clicks "Reports" in sidebar
   - Navigates to `/dashboard/reports`
   - "Inventory Report" tab active by default

4. **View Inventory Report:** Manager reviews inventory metrics
   - Summary cards show:
     * Total Items: 156
     * Total Value: ₹ 42,50,000
     * Available Items: 124 (79%)
     * Sold Items: 32 (21%)
   - Views pie chart: "Inventory by Category"
     * Rings: 45 items
     * Necklaces: 38 items
     * Bracelets: 28 items
     * Earrings: 45 items
   - Views bar chart: "Inventory by Material"
     * Gold: 65 items
     * Silver: 42 items
     * Diamond: 28 items
     * Platinum: 21 items

5. **Apply Filters:** Manager filters by category
   - Selects "Necklaces" from category dropdown
   - Charts and stats update to show only necklaces
   - Total items: 38
   - Available: 30, Sold: 8
   - Material breakdown for necklaces shown

6. **Switch to Sales Report:** Manager clicks "Sales Report" tab
   - Views sales metrics for default period (Last 30 Days)
   - Summary cards show:
     * Total Orders: 47
     * Completed Orders: 38 (81%)
     * Total Revenue: ₹ 18,50,000
     * Pending Orders: 9

7. **Change Date Range:** Manager selects custom date range
   - Clicks "Custom" in date range picker
   - Selects start date: "1 Jan 2024"
   - Selects end date: "31 Jan 2024"
   - Clicks "Apply"
   - GET /api/reports/sales?start_date=...&end_date=...
   - Charts and stats update for January

8. **Analyze Sales Trend:** Manager views line chart
   - "Sales Trend" shows daily revenue for January
   - Identifies peak days and slow periods
   - Hover over data points to see exact amounts
   - Notes: "25 Jan had highest revenue: ₹ 3,20,000"

9. **Review Top Sellers:** Manager scrolls to "Top Selling Items" table
   - Views top 10 items:
     * #1: "Diamond Solitaire Ring" - 8 sold - ₹ 6,40,000
     * #2: "Gold Chain Necklace" - 12 sold - ₹ 4,80,000
     * #3: "Silver Bracelet Set" - 15 sold - ₹ 3,00,000
   - Clicks on item code to view item details
   - Navigates to item detail page

10. **Return to Dashboard:** Manager clicks "Dashboard" in sidebar
    - Returns to overview
    - Mental note of insights gained from reports

**Success Criteria:**
- Manager can access reports (staff cannot)
- Charts render correctly with accurate data
- Filters and date ranges work as expected
- Data matches order and inventory records
- Reports load within 2 seconds

**Alternate Flows:**
- If no sales in date range: Show empty state with message
- Manager can export reports (MVP: shows "Coming soon" toast)
- Manager can navigate to orders directly from pending orders card
- Manager has all staff permissions (can add inventory, update orders)

---

## Implementation Checklist

Use this checklist to ensure all pages, features, and user flows are implemented:

### Pages
- [ ] Landing page (public catalog) with all sections
  - [ ] Hero section with headline, subheadline, CTA buttons
  - [ ] Logo generated and implemented
  - [ ] Features section with 4 features
  - [ ] Product grid with filters and search
  - [ ] Testimonials section with 3 testimonials
  - [ ] CTA section
  - [ ] Footer with contact info and links
- [ ] Item detail page with image gallery and specifications
- [ ] Login page with form validation
- [ ] Dashboard home (overview) with stats cards
- [ ] Inventory management page with data table
- [ ] Order management page with orders table
- [ ] Reports page with inventory and sales tabs (manager/owner only)
- [ ] User management page (owner only)

### Popups/Dialogs
- [ ] Order placement dialog with customer form
- [ ] Add/edit inventory item dialog with validation
- [ ] Order detail drawer with timeline
- [ ] Contact us dialog with business info
- [ ] Delete confirmation dialog

### Navigation & Access Control
- [ ] Sidebar navigation with role-based menu items
- [ ] Login redirects to appropriate dashboard
- [ ] Protected routes check authentication
- [ ] Role-based feature visibility (reports for manager+, users for owner)
- [ ] Active page indicator in navigation

### User Flow 1: Customer Browsing & Ordering
- [ ] Customer can browse landing page
- [ ] Product grid loads with all available items
- [ ] Category and material filters work correctly
- [ ] Search functionality filters products
- [ ] Clicking product card navigates to detail page
- [ ] Item detail page shows all information
- [ ] "Add to Order" opens order dialog
- [ ] Order form validates all required fields
- [ ] Successful order shows confirmation
- [ ] Order stored with "pending" status

### User Flow 2: Staff Inventory & Orders
- [ ] Staff can log in with valid credentials
- [ ] Dashboard shows relevant stats for staff role
- [ ] "Add New Item" dialog opens and validates
- [ ] Item code uniqueness is enforced
- [ ] New item appears in inventory table immediately
- [ ] Orders table shows all orders with filters
- [ ] Order detail drawer displays complete information
- [ ] Status update dropdown shows valid transitions
- [ ] Order status updates successfully
- [ ] Changes reflected in real-time

### User Flow 3: Manager Reports
- [ ] Manager login works and identifies role
- [ ] Reports menu item visible to manager (not staff)
- [ ] Inventory report loads with correct data
- [ ] Charts render properly (pie, bar, donut)
- [ ] Category/material filters update report
- [ ] Sales report tab switches correctly
- [ ] Date range picker works (quick filters + custom)
- [ ] Sales charts show accurate trend data
- [ ] Top selling items table displays correctly
- [ ] Clicking item navigates to detail page

### API Integration
- [ ] POST /api/auth/login returns JWT token
- [ ] GET /api/auth/me fetches current user
- [ ] GET /api/inventory/items loads catalog (public + authenticated)
- [ ] POST /api/inventory/items creates new item
- [ ] PATCH /api/inventory/items/{id} updates item
- [ ] POST /api/orders places new order (public)
- [ ] GET /api/orders fetches all orders (staff+)
- [ ] PATCH /api/orders/{id}/status updates status
- [ ] GET /api/reports/inventory returns inventory stats (manager+)
- [ ] GET /api/reports/sales returns sales data (manager+)

### Design System Implementation
- [ ] Rose gold, burgundy, bronze color palette applied
- [ ] Cormorant Garamond font for public catalog headings
- [ ] Inter font for admin dashboard
- [ ] JetBrains Mono for item codes and data
- [ ] Lucide icons used throughout
- [ ] Hover effects: lift, scale, border animations
- [ ] Loading states with shimmer effect
- [ ] Empty states with illustrations
- [ ] Status badges color-coded correctly
- [ ] Responsive breakpoints (mobile/tablet/desktop)

### Accessibility
- [ ] All images have alt text
- [ ] Keyboard navigation works on all pages
- [ ] Focus states visible with rose gold ring
- [ ] Form fields have labels and error messages
- [ ] Required fields marked clearly
- [ ] ARIA labels on interactive elements
- [ ] Screen reader tested for critical flows

### Polish & Final Touches
- [ ] All transitions smooth (300-400ms)
- [ ] Success toasts appear for user actions
- [ ] Error messages clear and helpful
- [ ] Loading spinners during API calls
- [ ] Tooltips on hover where helpful
- [ ] Print-friendly styles (future: receipt printing)
- [ ] Dark mode toggle in settings (optional)
- [ ] Images optimized (WebP with fallbacks)

---

## Notes for Developers

### MVP Scope
This is a minimal viable product focused on core functionality:
- Public catalog browsing
- COD order placement
- Staff inventory management
- Order status updates
- Basic reporting for managers

### Out of Scope for v1
- User registration/signup (users created by admin)
- Online payments (only COD)
- Customer accounts and order history
- Advanced search (full-text search)
- Image uploads (use URLs for now)
- PDF/Excel export of reports
- Email notifications
- Low stock alerts
- Bulk operations
- Soft delete for items

### Technical Implementation
- Use React for frontend with React Router for navigation
- Use Axios for API calls with interceptors for JWT
- Store JWT token in localStorage
- Implement role-based rendering using React context
- Use shadcn/ui components as base (customize with design system colors)
- Tailwind CSS for styling with custom theme configuration
- Lucide React for icons
- Recharts or similar for report visualizations
- React Hook Form for form validation
- Date-fns for date formatting

### Environment Variables
- `REACT_APP_API_URL`: Backend API base URL (default: http://localhost:8001)
- Backend handles MONGO_URL, JWT_SECRET, etc.

### Data Handling
- Prices stored in cents in backend, display as rupees (divide by 100)
- Dates in ISO 8601 format, display in user-friendly format
- Pagination default: 20 items per page
- Cache dashboard stats for 5 minutes (stale-while-revalidate)

### Image Strategy
For MVP, use one of these approaches:
1. External URLs: Store full URLs in images array
2. Stock photos: Use Unsplash/Pexels for sample jewellery images
3. Placeholder service: Use placeholder.com with product dimensions
4. AI-generated: Generate product images using image generation tools

Future enhancement: Implement file upload endpoint for direct image uploads

### Deployment Considerations
- Static assets: Serve via CDN
- Images: Optimize and serve via CDN (future)
- API: Separate backend deployment
- CORS: Configure backend for frontend domain
- HTTPS required for production
- Environment-specific API URLs

### Testing Strategy
- Test all three user flows end-to-end
- Test role-based access (staff cannot access reports)
- Test form validations (client-side and server-side)
- Test order placement with invalid items
- Test duplicate item code prevention
- Cross-browser testing (Chrome, Firefox, Safari)
- Responsive testing on mobile devices

---

## Summary

This UX plan defines a complete jewellery store management system with:
- **8 main pages**: Landing, item detail, login, dashboard home, inventory, orders, reports, user management
- **5 popups/dialogs**: Order placement, add/edit item, order details, contact us, delete confirmation
- **3 complete user flows**: Customer ordering, staff operations, manager analytics
- **Role-based access**: Public, staff, manager, owner with appropriate permissions
- **Luxury design system**: Rose gold theme with elegant typography and smooth interactions
- **MVP-focused**: Core features only, clear roadmap for future enhancements

The system balances elegant customer-facing design with efficient admin functionality, ensuring both jewelry buyers and store staff have optimal experiences.