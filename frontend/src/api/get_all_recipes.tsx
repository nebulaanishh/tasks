import { useEffect, useState } from "react";
import axios from "axios";


function useFetch(url: string) {
    const [data, setData] = useState<any>([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    useEffect(() => {
        setLoading(true)
        setData(null);
        setError(false);
        // const source = axios.CancelToken.source();
        axios.get(url)
            .then(res => {
                setLoading(false);
                
                res.data && setData(res.data);
            })
            .catch(err => {
                setLoading(false)
                setError(true)
                console.log(err)
            })
        return () => {
            // source.cancel();
        }
    }, [url])

    return { data, loading, error }
}

export default useFetch