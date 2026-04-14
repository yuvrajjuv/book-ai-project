import { useState } from "react";

function App() {
  const [books, setBooks] = useState([]);

  // ✅ GET BOOKS
  const getBooks = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/books/");
    const data = await res.json();
    setBooks(data);
  };

  // ✅ SCRAPE BOOKS
  const scrapeBooks = async () => {
    await fetch("http://127.0.0.1:8000/api/books/scrape/");
    alert("Scraping Done!");
  };

  // ✅ GENERATE AI (FAKE)
  const generateAI = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/books/generate-ai/");
    const data = await res.json();
    setBooks(data);
  };

  return (
    <div
      style={{
        textAlign: "center",
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "20px",
      }}
    >
      <h1 style={{ fontSize: "40px", marginBottom: "20px" }}>
        📚 Book AI Project
      </h1>

      {/* 🔥 BUTTONS */}
      <div style={{ marginBottom: "20px" }}>
        <button onClick={getBooks}>Get Books</button>{" "}
        <button onClick={scrapeBooks}>Scrape Books</button>{" "}
        <button onClick={generateAI}>Generate AI</button>
      </div>

      {/* 🔥 BOOK LIST */}
      {books.map((book, index) => (
        <div
          key={index}
          style={{
            borderBottom: "1px solid gray",
            padding: "15px",
            marginBottom: "10px",
          }}
        >
          <h2>{book.title}</h2>
          <p>{book.author}</p>

          {/* ✅ SUMMARY SHOW */}
          {book.summary && (
            <p style={{ color: "#ccc", marginTop: "10px" }}>
              {book.summary}
            </p>
          )}
        </div>
      ))}
    </div>
  );
}

export default App;