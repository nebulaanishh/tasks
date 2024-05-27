import { Link } from "react-router-dom";
import useFetch from "../api/get_all_recipes";
import Hero from "../components/Hero";
import Card from "../components/card";
import Layout from "../layout/Layout";
import { useNavigate } from "react-router-dom";
import Cards from "../components/allCards";


function RecipeList() {
    const { data: items, loading, error } = useFetch('http://localhost:8000/recipes/')
    const navigate = useNavigate();



    if (loading) return <span>Loading...</span>
    if (error) return <span>Something went wrong...</span>

    return (
        <>
            <Layout>
                <Cards items={items} />
            </Layout>


        </>
    )
}

export default RecipeList