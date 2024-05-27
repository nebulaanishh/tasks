import useFetch from "../api/get_all_recipes"
import Card from "./card";

interface DetailCardProps {
    id: number|string; 
  }

export default function DetailCard({ id }: DetailCardProps) {
    const { data: item, loading, error } = useFetch('http://localhost:8000/recipes/' + id)

    if (loading) return <span>Loading...</span>;
    if (error) return <span>Something went wrong...</span>;
    
    return (
        <>
            {item && (
                <div className="w-8/12 bg-slate-200 mx-auto m-20 rounded-lg flex">
                    <img className="p-4 rounded-lg" width={400} src={item.image} alt="" />
                    <div className="mx-auto">
                        <h1 className="font-bold text-green-600 m-6 text-3xl"> {item.name} </h1>
                    <div className="p-4 font-medium text-small">
                        {console.log(item)}
                    {item.instructions.split('.').map( (i, index) => (
                         <li key={index}> {i.trim()} </li>
                    ) )}
                    </div>
                    </div>
                </div>
                
            )}
        </>
    )
}