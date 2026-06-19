import http from "k6/http";

export default function () {
  const username = `user_${Math.floor(Math.random() * 1000000)}`;

  if (Math.random() < 0.5) {
    http.post(
      `http://10.1.43.116:8080/bloom/add`,
      JSON.stringify({ value: username }),
      {
        headers: { "Content-Type": "application/json" },
      },
    );
    // http.post(`http://10.1.43.116:8080/bloom/add/${username}`);
  } else {
    http.get(`http://10.1.43.116:8080/bloom/username/${username}`);
  }
}

// k6 run --vus 100 --iterations 100000 k6_test.js
