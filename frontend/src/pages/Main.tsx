import HeroSection from "@/components/main/HeroSection";
import Navbar from "../components/main/Navbar";
import TopPart from '@/components/main/TopPart';
import Categories from "@/components/main/Categories";
import Products from "@/components/main/Products";
import Footer from "@/components/main/Footer";
import BusinessRegistration from "@/components/main/BusinessRegistration";
import { HowItWorks } from "@/components/main/HowItWorks";
import { TradeWithConfidence } from "@/components/main/TradeWithConfidence";
import { SADCConnections } from "@/components/main/SadcConnections";


const Main = () => {
    return (
        <>
            <div className="flex flex-col w-full h-full bg-[#172554]">
                <TopPart />
                <Navbar />
                <HeroSection />

            </div>
            <div className="flex flex-col w-full h-full mb-12">
                <Categories />
                <Products />
                <BusinessRegistration />
                <HowItWorks />
                <TradeWithConfidence />
                <SADCConnections />
            </div>
            <div className="">
                <Footer />
            </div>
        </>
    );
};

export default Main;
