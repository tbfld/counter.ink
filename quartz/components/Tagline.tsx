import { QuartzComponentConstructor, QuartzComponentProps } from "./types";

const Tagline: QuartzComponentConstructor = () => {
 function TaglineComponent() {
   return (
     <div style={{ fontSize: "0.85em", color: "var(--gray)", marginTop: "-10px", paddingBottom: "10px" }}>
       ted byfield
     </div>
   );
 }

 return TaglineComponent;
};

export default Tagline;