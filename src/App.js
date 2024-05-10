import React, { useState, useEffect } from "react";
import axios from "axios";

const NewsComponent = () => {
  const [headlines, setHeadlines] = useState([]);

  useEffect(() => {
    const fetchHeadlines = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/headlines");
        setHeadlines(response.data.articles);
      } catch (error) {
        console.error("Error fetching headlines:", error);
      }
    };

    fetchHeadlines();
  }, []);

  return (
    <div>
      <h2>Latest Headlines</h2>
      <ul>
        {headlines.map((headline, index) => (
          <li key={index}>
            <a href={headline.url}>{headline.title}</a> - {headline.source.name}{" "}
            ({new Date(headline.publishedAt).toDateString()})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsComponent;