package cp213;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Utilities for working with Movie objects.
 *
 * @author Solomon Olufelo, 210729170, oluf9170@mylaurier.ca
 * @version 2025-10-18
 */
public class MovieUtilities {

    /**
     * Counts the number of movies in each genre given in {@code Movie.GENRES}. An
     * empty movies list should produce a count array of: [0,0,0,0,0,0,0,0,0,0,0]
     *
     * @param movies {@code List} of movies
     * @return number of genres across all movies - one entry for each genre in the
     *         {@code Movie.GENRES} array
     */
    public static int[] genreCounts(final ArrayList<Movie> movies) {
	int[] counts = new int[Movie.GENRES.length];
	for (Movie movie : movies) {
	    if (movie.getGenre() >= 0 && movie.getGenre() < counts.length) {
		counts[movie.getGenre()]++;
	    }
	}
	return counts;
    }

    /**
     * Creates a {@code Movie} object by requesting data from a user. Uses the
     * format:
     *
     * <pre>
    Title:
    Year:
    Director:
    Rating:
    Genres:
     0: science fiction
     1: fantasy
    ...
    10: mystery

    Enter a genre number:
     * </pre>
     *
     * @param keyboard a keyboard ({@code System.in}) {@code Scanner} object
     * @return a {@code Movie} object.
     */
    public static Movie getMovie(final Scanner keyboard) {
	System.out.print("Title: ");
	String title = keyboard.nextLine();
	
	System.out.print("Year: ");
	int year = keyboard.nextInt();
	keyboard.nextLine(); // consume newline
	
	System.out.print("Director: ");
	String director = keyboard.nextLine();
	
	System.out.print("Rating: ");
	double rating = keyboard.nextDouble();
	keyboard.nextLine(); // consume newline
	
	System.out.println("Genres:");
	System.out.print(Movie.genresMenu());
	System.out.print("Enter a genre number: ");
	int genre = keyboard.nextInt();
	keyboard.nextLine(); // consume newline
	
	return new Movie(title, year, director, rating, genre);
    }

    /**
     * Creates a {@code List} of movies whose genre is equal to the {@code genre}
     * parameter.
     *
     * @param movies {@code List} of movies
     * @param genre  genre to compare against
     * @return {@code List} of movies of type {@code genre}
     */
    public static ArrayList<Movie> getByGenre(final ArrayList<Movie> movies, final int genre) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie movie : movies) {
	    if (movie.getGenre() == genre) {
		result.add(movie);
	    }
	}
	return result;
    }

    /**
     * Creates a {@code List} of Movies whose ratings are equal to or higher than
     * rating.
     *
     * @param movies {@code List} of movies
     * @param rating rating to compare against
     * @return {@code List} of movies of {@code rating} or higher
     */
    public static ArrayList<Movie> getByRating(final ArrayList<Movie> movies, final double rating) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie movie : movies) {
	    if (movie.getRating() >= rating) {
		result.add(movie);
	    }
	}
	return result;
    }

    /**
     * Creates a {@code List} of Movies from a particular year.
     *
     * @param movies {@code List} of movies
     * @param year   year to compare against
     * @return {@code List} of movies of year
     */
    public static ArrayList<Movie> getByYear(final ArrayList<Movie> movies, final int year) {
	ArrayList<Movie> result = new ArrayList<>();
	for (Movie movie : movies) {
	    if (movie.getYear() == year) {
		result.add(movie);
	    }
	}
	return result;
    }

    /**
     * Asks a user to select a genre from a list of genres displayed by calling
     * {@code Movie.genresMenu} and returns an integer genre code. The genre must be
     * a valid index to an item in Movie.GENRES.
     *
     * @param keyboard a keyboard ({@code System.in}) {@code Scanner} object
     * @return an integer genre code
     */
    public static int readGenre(final Scanner keyboard) {
	int genre;
	do {
	    System.out.print(Movie.genresMenu());
	    System.out.print("Enter a genre number: ");
	    genre = keyboard.nextInt();
	    keyboard.nextLine(); // consume newline
	} while (genre < 0 || genre >= Movie.GENRES.length);
	return genre;
    }

    /**
     * Creates and returns a {@code Movie} object from a line of formatted string
     * data. The data should be in the format:
     *
     * <pre>
     * "title|year|director|rating|genre"
     * </pre>
     *
     * The quote character (") is not part of the string. See the file movies.txt
     * for an example of the file format and contents.
     *
     * @param line A vertical bar-delimited line of movie data
     *
     * @return the data from line as a {@code Movie} object
     */
    public static Movie readMovie(final String line) {
	String[] parts = line.split("\\|");
	if (parts.length == 5) {
	    String title = parts[0];
	    int year = Integer.parseInt(parts[1]);
	    String director = parts[2];
	    double rating = Double.parseDouble(parts[3]);
	    int genre = Integer.parseInt(parts[4]);
	    return new Movie(title, year, director, rating, genre);
	}
	return null;
    }

    /**
     * Reads a {@code List} of Movies from a file. Each line of the file is in the
     * format:
     *
     * <pre>
     * "title|year|director|rating|genre"
     * </pre>
     *
     * The quote character (") is not part of the string. See the file movies.txt
     * for an example of the file format and contents.
     *
     * @param fileIn a {@code Scanner} of a movie data file
     *
     * @return a {@code List} of movies
     */
    public static ArrayList<Movie> readMovies(final Scanner fileIn) {
	ArrayList<Movie> movies = new ArrayList<>();
	while (fileIn.hasNextLine()) {
	    String line = fileIn.nextLine().trim();
	    if (!line.isEmpty()) {
		Movie movie = readMovie(line);
		if (movie != null) {
		    movies.add(movie);
		}
	    }
	}
	return movies;
    }

    /**
     * Writes the contents of a {@code List} of movies to a {@code PrintStream}.
     *
     * @param movies {@code List} of movies
     * @param ps     output {@code PrintStream}
     */
    public static void writeMovies(final ArrayList<Movie> movies, PrintStream ps) {
	for (Movie movie : movies) {
	    movie.write(ps);
	}
    }

}
