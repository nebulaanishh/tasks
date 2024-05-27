import { useNavigate } from "react-router-dom";
import Card from "./card";

export default function Cards({ items }) {
    const navigate = useNavigate();
    const handleClick = (id) => {
        navigate(`/recipes/${id}`);
    }
    return (
        <>
            <h1 className="pt-20 text-center font-semibold text-4xl">Featured Recipes</h1>
            <div className="grid grid-cols-3 gap-10 pt-10 px-56">
                {items?.map((item: any) => (
                    <div key={item.id} onClick={() => handleClick(item.id)}>
                        <Card item={item} />
                    </div>
                ))}
            </div>
        </>
    )
}