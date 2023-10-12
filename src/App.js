import  { useState, useEffect} from "react";
import MovieCard from "./MovieCard";
 //ca7e8933
 import './App.css';
 import SearchIcon from './search.svg';

const movie1 = {
  "Title": "Batman Begins",
  "Year": "2005",
  "imdbID": "tt0372784",
  "Type": "movie",
  "Poster": "https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"
}
 const APIURL = 'http://www.omdbapi.com/?i=tt3896198&apikey=ca7e8933'
const App = () => {
 const [movies, setMovies] = useState([]);
 const [searchTerm,setSearchTerm] = useState('');
 const [title, setTitle] = useState('batman');
  const searchMovies = async (title) => {
    if(title){
    const response = await fetch(`${APIURL}&s=${title}`);
    const data = await response.json();
    console.log(data);
    setMovies(data.Search);
    } else{
    const response = await fetch(`${APIURL}`);
    const data = await response.json();
    console.log(data);
    setMovies(data);
    }
    console.log(movies)
  }
  useEffect(() =>
  {
    setTitle(searchTerm);
  }, [searchTerm]);

  useEffect(() =>
  {
    searchMovies(title);
  }, []);
  return (
    <div className="app">
      <h1>MovieLand</h1>
      <div className="search">
        <input
        placeholder="Search for movies"
        value={searchTerm}
        onChange={(e) => {setSearchTerm(e.target.value)}}
        />
        <img src={SearchIcon}
        alt="search"
        onClick={() => {searchMovies(title)}}
        />
      </div>

      {
        movies?.length > 0
        ? (
          <div className="container">
            {movies.map((movie) => (
              <MovieCard movie={movie}/>
            ))}
      </div>
        ) : (
          <div className="empty">
            <h2>No movies found</h2>
          </div>
        )
      }
    </div>
  );
}

export default App;