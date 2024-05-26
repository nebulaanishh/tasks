import useFetch from "../api/get_all_recipes";
import Hero from "../components/Hero";
import Card from "../components/card";
import Layout from "../layout/Layout";


function Homepage(){
    const itemss= [
        {
            "id": 181,
            "name": "Classic Margherita Pizza",
            "instructions": "Preheat the oven to 475°F (245°C). Roll out the pizza dough and spread tomato sauce evenly. Top with slices of fresh mozzarella and fresh basil leaves. Drizzle with olive oil and season with salt and pepper. Bake in the preheated oven for 12-15 minutes or until the crust is golden brown. Slice and serve hot.",
            "cook_time_minutes": 15,
            "servings": 4,
            "difficulty": "Easy",
            "cuisine": "Italian",
            "calories_per_serving": 300,
            "image": "https://cdn.dummyjson.com/recipe-images/1.webp",
            "rating": "4.6",
            "ingredients": {
                "ingredients": [
                    "Pizza dough",
                    "Tomato sauce",
                    "Fresh mozzarella cheese",
                    "Fresh basil leaves",
                    "Olive oil",
                    "Salt and pepper to taste"
                ]
            },
            "tags": {
                "tags": [
                    "Pizza",
                    "Italian"
                ]
            }
        },
    ]

    const {data: items, loading, error}= useFetch('http://localhost:8000/recipes/') 

    console.log(error)

    if(loading) return <span>Loading...</span>
    if(error) return <span>Something went wrong...</span>
    return (
        <>
        <Layout>
            <Hero />
            {items?.map((item:any) => (
            <Card  item={item} />
            ) )}

            
        </Layout>


        </>
    )
}

export default Homepage