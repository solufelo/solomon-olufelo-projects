import { mockMovies } from '../lib/mockData'
import MovieCard from '../components/MovieCard'
import Navbar from "../components/Navbar"


export default function Home() {
  return (
    <main className="bg-gray-500 text-white min-h-screen p-4">
   <Navbar />
      <h1 className="text-4xl font-bold text-white mb-8">Popular Movies</h1>
      {/* Navbar */}
     
      {/* Movie Cards Grid */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
        {mockMovies.map(movie => (
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>
    </main>
  )
}