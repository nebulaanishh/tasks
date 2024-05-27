import { useEffect, useState } from "react";
import axios from "axios";


function useFetch(url: string) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);
  
    useEffect(() => {
      setLoading(true);
      setData(null);
      setError(false);
  
      axios.get(url)
        .then(res => {
          setLoading(false);
          res.data && setData(res.data);
        })
        .catch(err => {
          setLoading(false);
          setError(true);
          console.error("Fetch error:", err); // Log the error
        });
  
    }, [url]);
  
    return { data, loading, error };
  }
  
  export default useFetch;