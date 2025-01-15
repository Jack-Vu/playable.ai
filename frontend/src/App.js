import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [data, setData] = useState(null);
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("image", image);
    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.log("Error", error);
      setLoading(false);
    }
  };

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-slate-700 via-gray-900 to-slate-700 text-base-content flex flex-col items-center">
      <header className="py-6 text-center">
        <h1 className="text-3xl font-bold text-gray-300">🎮Playable.ai</h1>
        <p className="text-md mt-2 text-gray-400">
          Scan an object to discover fun games to play!
        </p>
      </header>
      <form
        className="bg-purple-600 p-6 rounded-lg shadow-md w-full max-w-md space-y-4"
        onSubmit={handleSubmit}
      >
        <h2 className="text-2xl font-semibold text-center text-white">
          Upload Your Image
        </h2>
        <input
          type="file"
          onChange={handleImageChange}
          className="w-full p-2 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="w-full p-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-200"
        >
          Upload Image
        </button>
      </form>
      {loading && (
        <div className="mt-4 flex justify-center">
          <div className="w-16 h-16 border-t-4 border-blue-600 border-solid rounded-full animate-spin"></div>
        </div>
      )}
      {data ? (
        <div className="flex flex-col justify-center items-center gap-4 mt-4">
          <div className="text-gray-300 text-2xl">Suggested Games:</div>
          <div className="text-white bg-green-500 p-4 rounded-lg shadow-md mx-auto w-[50%]">
            <p>{data}</p>
          </div>
        </div>
      ) : null}
    </div>
  );
};

export default App;
