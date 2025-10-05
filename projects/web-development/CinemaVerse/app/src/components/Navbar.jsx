export default function Navbar() {
  return (
    <nav className="flex items-center justify-between px-6 py-4 bg-gray-800 shadow-lg">
      <h1 className="text-2xl font-bold text-red-600">🎬 Cinemaverse</h1>
      <div className="space-x-4">
        <button className="text-white hover:underline">Login</button>
      </div>
    </nav>
  )
}
