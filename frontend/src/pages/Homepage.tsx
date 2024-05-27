import { Link } from "react-router-dom";
import useFetch from "../api/get_all_recipes";
import Hero from "../components/Hero";
import Card from "../components/card";
import Layout from "../layout/Layout";
import { useNavigate } from "react-router-dom";


function Homepage() {
    const { data: items, loading, error } = useFetch('http://localhost:8000/recipes/')
    const navigate = useNavigate();

    const handleClick = (id) => {
        navigate(`/recipes/${id}`);
    }

    if (loading) return <span>Loading...</span>
    if (error) return <span>Something went wrong...</span>

    return (
        <>
            <Layout>
                <Hero />
                {items?.map((item: any) => (
                    <div key={item.id} onClick= { () => handleClick(item.id)}>
                        <Card  item={item} />
                    </div>
                ))}


            </Layout>


        </>
    )
}

export default Homepage