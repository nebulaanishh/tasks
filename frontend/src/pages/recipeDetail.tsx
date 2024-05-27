import { useParams } from "react-router-dom";
import useFetch from "../api/get_all_recipes";
import DetailCard from "../components/detailCard";
import Layout from "../layout/Layout";

export default function RecipeDetail() {
    const { id } = useParams();

    return (
        <Layout>
            <DetailCard id={id} />
        </Layout>
    )
}