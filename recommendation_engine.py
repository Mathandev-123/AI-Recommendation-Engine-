import numpy as np

def run_recommendation_pipeline():
    print("=" * 60)
    print("          DECODELABS AI INTERNSHIP - PROJECT 3          ")
    print("      AI RECOMMENDATION LOGIC ENGINE (PYROID 3 READY)   ")
    print("=" * 60)
    
    # --------------------------------------------------
    # STEP 1: DATA DEFINITION (Shared Vocabulary & Items Dataset)
    # --------------------------------------------------
    # Exact vector mapping vocabulary space to prevent discrepancies
    vocabulary = [
        "python", "web development", "machine learning", "data science", 
        "javascript", "react", "cloud computing", "automation", "sql", "algorithms"
    ]
    
    # Intrinsic item properties dictionary (Content-Based Attributes)
    course_items = {
        "Course A: Modern Web Architectures": ["web development", "javascript", "react"],
        "Course B: Applied Machine Learning & Data Science": ["python", "machine learning", "data science", "algorithms"],
        "Course C: Cloud Automation & DevOps": ["cloud computing", "automation", "python"],
        "Course D: Advanced Database Systems & SQL": ["sql", "algorithms"],
        "Course E: Full-Stack Engineering Blueprint": ["web development", "javascript", "react", "python", "sql"],
        "Course F: Foundations of AI Engineering": ["python", "machine learning", "algorithms"]
    }
    
    print("\n[1/4] Content-Based Database Initialized Successfully.")
    print(f"-> Total Items in Catalog: {len(course_items)}")
    print(f"-> Shared Vocabulary Dimensions: {len(vocabulary)}")
    
    # --------------------------------------------------
    # STEP 2: INPUT LAYER (Capture User Profile State)
    # --------------------------------------------------
    print("\n[2/4] --- USER INTEREST INTERACTIVE PROFILE ---")
    print("Available tags to select from:")
    for idx, tag in enumerate(vocabulary, 1):
        print(f" {idx}. {tag.title()}")
        
    print("\nEnter corresponding numbers separated by commas (e.g., 1,3,4):")
    user_choice = input("Your Selections: ").strip()
    
    # Default selection if user leaves it empty to prevent crashing
    if not user_choice:
        user_choice = "1,3"
        print("-> No interaction captured. Defaulting to: Python, Machine Learning.")
        
    # Process user choices into selected keywords
    user_selected_tags = []
    try:
        indices = [int(i.strip()) - 1 for i in user_choice.split(",") if i.strip().isdigit()]
        for idx in indices:
            if 0 <= idx < len(vocabulary):
                user_selected_tags.append(vocabulary[idx])
    except ValueError:
        user_selected_tags = ["python", "machine learning"]
        
    if not user_selected_tags:
        user_selected_tags = ["python", "machine learning"]
        
    print(f"-> Captured Explicit User Profile Tags: {user_selected_tags}")
    
    # Vector Mapping: Transform qualitative selections into binary vectors
    user_vector = np.array([1 if tag in user_selected_tags else 0 for tag in vocabulary])
    print(f"-> User Profile Vector: {user_vector}")
    
    # --------------------------------------------------
    # STEP 3: PROCESS LAYER (Apply Mathematical Similarity Logic)
    # --------------------------------------------------
    print("\n[3/4] Running Similarity Alignment Matrix...")
    recommendation_scores = {}
    
    for item_name, item_tags in course_items.items():
        # Map item attributes to the exact same vocabulary space
        item_vector = np.array([1 if tag in item_tags else 0 for tag in vocabulary])
        
        # Calculate Jaccard Similarity: Size of Intersection / Size of Union
        intersection = np.sum(np.logical_and(user_vector, item_vector))
        union = np.sum(np.logical_or(user_vector, item_vector))
        
        # Avoid zero division fallback
        jaccard_score = intersection / union if union > 0 else 0.0
        recommendation_scores[item_name] = (jaccard_score, item_vector)
        
    print("-> Pattern alignment vectors calculated correctly.")
    
    # --------------------------------------------------
    # STEP 4: OUTPUT LAYER (Generate Top-N Tailored List)
    # --------------------------------------------------
    print("\n[4/4] Generating Truncated Top Recommendations...")
    print("-" * 60)
    print("                   FINAL TAILORED RECON REPORT          ")
    print("-" * 60)
    
    # Sort courses based on mathematical similarity score in descending order
    sorted_recommendations = sorted(recommendation_scores.items(), key=lambda x: x[1][0], reverse=True)
    
    rank = 1
    for item_name, (score, item_vector) in sorted_recommendations:
        # Filter matching status
        status = "🔥 Recommended Match" if score > 0 else "❄️ Low Match/Alternative"
        print(f"\nRank #{rank}: {item_name} [{status}]")
        print(f" ╰─> Similarity Alignment Score: {score:.4f} ({score * 100:.1f}%)")
        print(f" ╰─> Structural Vector Shape  : {item_vector.tolist()}")
        rank += 1
        
    print("=" * 60)
    print("Recommendation engine execution complete. Portfolio asset validated!")

if __name__ == "__main__":
    run_recommendation_pipeline()