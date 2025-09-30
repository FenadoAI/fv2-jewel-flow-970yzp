import { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8001';
const API = `${API_BASE}/api`;

function HomePage() {
  const navigate = useNavigate();
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    category: '',
    material: '',
    search: ''
  });

  useEffect(() => {
    fetchItems();
  }, [filters]);

  const fetchItems = async () => {
    try {
      setLoading(true);
      const params = new URLSearchParams();
      if (filters.category) params.append('category', filters.category);
      if (filters.material) params.append('material', filters.material);
      if (filters.search) params.append('search', filters.search);

      const response = await axios.get(`${API}/inventory/items?${params.toString()}`);
      setItems(response.data.items);
    } catch (error) {
      console.error('Error fetching items:', error);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['ring', 'necklace', 'bracelet', 'earring', 'pendant'];
  const materials = ['gold', 'silver', 'diamond', 'platinum', 'ruby', 'emerald'];

  return (
    <div className="min-h-screen bg-gradient-to-br from-rose-50 to-amber-50">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <h1 className="text-3xl font-bold text-rose-700">LuxeGems</h1>
            <button
              onClick={() => navigate('/login')}
              className="px-4 py-2 border-2 border-rose-600 text-rose-600 rounded-lg hover:bg-rose-600 hover:text-white transition"
            >
              Staff Login
            </button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="bg-gradient-to-r from-rose-600 to-amber-600 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-5xl font-bold mb-4">Discover Timeless Elegance</h2>
          <p className="text-xl mb-8">
            Browse our curated collection of fine jewellery, crafted with precision and delivered with care.
            Shop from the comfort of your home with Cash on Delivery.
          </p>
          <button
            onClick={() => document.getElementById('collection').scrollIntoView({ behavior: 'smooth' })}
            className="bg-white text-rose-600 px-8 py-3 rounded-lg font-semibold hover:bg-rose-50 transition"
          >
            Explore Collection
          </button>
        </div>
      </section>

      {/* Filters */}
      <div id="collection" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* Search */}
            <input
              type="text"
              placeholder="Search by name or item code..."
              value={filters.search}
              onChange={(e) => setFilters({ ...filters, search: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-rose-500 focus:border-transparent"
            />

            {/* Category Filter */}
            <select
              value={filters.category}
              onChange={(e) => setFilters({ ...filters, category: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-rose-500 focus:border-transparent"
            >
              <option value="">All Categories</option>
              {categories.map(cat => (
                <option key={cat} value={cat}>{cat.charAt(0).toUpperCase() + cat.slice(1)}</option>
              ))}
            </select>

            {/* Material Filter */}
            <select
              value={filters.material}
              onChange={(e) => setFilters({ ...filters, material: e.target.value })}
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-rose-500 focus:border-transparent"
            >
              <option value="">All Materials</option>
              {materials.map(mat => (
                <option key={mat} value={mat}>{mat.charAt(0).toUpperCase() + mat.slice(1)}</option>
              ))}
            </select>
          </div>
        </div>

        {/* Product Grid */}
        {loading ? (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-rose-600"></div>
          </div>
        ) : items.length === 0 ? (
          <div className="text-center py-12 text-gray-500">
            <p>No items found matching your criteria.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {items.map((item) => (
              <div
                key={item.id}
                className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow cursor-pointer transform hover:scale-105 duration-200"
                onClick={() => navigate(`/item/${item.id}`)}
              >
                <div className="aspect-w-4 aspect-h-5 bg-gray-200">
                  {item.images && item.images.length > 0 ? (
                    <img src={item.images[0]} alt={item.name} className="w-full h-64 object-cover" />
                  ) : (
                    <div className="w-full h-64 flex items-center justify-center bg-gradient-to-br from-rose-100 to-amber-100">
                      <span className="text-4xl">💎</span>
                    </div>
                  )}
                </div>
                <div className="p-4">
                  <h3 className="text-lg font-semibold text-gray-900 mb-1">{item.name}</h3>
                  <p className="text-sm text-gray-500 font-mono mb-2">{item.item_code}</p>
                  <div className="flex items-center justify-between mb-2">
                    <span className="inline-block px-2 py-1 text-xs rounded-full bg-amber-100 text-amber-800">
                      {item.material}
                    </span>
                    <span className={`inline-block px-2 py-1 text-xs rounded-full ${
                      item.status === 'available' ? 'bg-green-100 text-green-800' :
                      item.status === 'reserved' ? 'bg-yellow-100 text-yellow-800' :
                      'bg-gray-100 text-gray-800'
                    }`}>
                      {item.status}
                    </span>
                  </div>
                  <p className="text-2xl font-bold text-rose-600">${(item.price / 100).toFixed(2)}</p>
                  <button className="mt-3 w-full bg-rose-600 text-white py-2 rounded-lg hover:bg-rose-700 transition">
                    View Details
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-lg font-semibold">LuxeGems - Elegance in Every Detail</p>
          <p className="text-sm text-gray-400 mt-2">© 2025 LuxeGems. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default HomePage;