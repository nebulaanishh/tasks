import useFetch from "../api/get_all_recipes"
import Card from "./card";

export default function DetailCard({ id }: any) {
    const { data: item, loading, error } = useFetch('http://localhost:8000/recipes/' + id)

    if (loading) return <span>Loading...</span>;
    if (error) return <span>Something went wrong...</span>;

    return (
        <>
            {item && (
                <div className="w-8/12 bg-slate-200 mx-auto m-20 rounded-md flex">
                    <img width={600} src={item.image} alt="" />
                    <div className="mx-auto">
                        <h1 className="font-bold text-green-600 m-6 text-3xl"> {item.name} </h1>
                    </div>
                </div>
                
            )}
        </>
    )
}