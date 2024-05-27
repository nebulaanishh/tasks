import useFetch from "../api/get_all_recipes"
import Card from "./card";

export default function DetailCard( {id}:any ){
    const { data: item, loading, error } = useFetch('http://localhost:8000/recipes/' + id)

    if (loading) return <span>Loading...</span>;
    if (error) return <span>Something went wrong...</span>;

    return (
        <>
          {item && (
                <div>
                    <Card item={item} /> 
                </div>
            )}
        </>
    )
}