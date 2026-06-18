import http from "k6/http";

export default function () {
  const username = `user_${Math.floor(Math.random() * 1000000)}`;

  if (Math.random() < 0.1) {
    http.post("http://localhost:8000/usernames", JSON.stringify({ username }), {
      headers: { "Content-Type": "application/json" },
    });
  } else {
    http.get(`http://localhost:8000/usernames/${username}`);
  }
}

// k6 run --vus 100 --iterations 100000 k6_test.js
