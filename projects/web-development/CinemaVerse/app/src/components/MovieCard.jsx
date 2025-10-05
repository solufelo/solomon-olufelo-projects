export default function MovieCard({ movie }) {
  return (
    <div className="bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:scale-105 transition-transform">
      <img 
  src={movie.poster_path 
    ? `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    : '/placeholder-movie.jpg'
  }
  alt={movie.title}
  className="w-full h-64 object-cover"
/>
      <div className="p-4">
        <h3 className="font-bold truncate">{movie.title}</h3>
        <div className="flex justify-between text-sm text-gray-400">
          <span>{movie.release_date.substring(0,4)}</span>
          <span>⭐ {movie.vote_average.toFixed(1)}</span>
        </div>
      </div>
    </div>
  )
}