#!/usr/bin/env python3
"""Scientific rigor validation for consciousness blob processing"""

import asyncio
import aiohttp
import json
import time
import statistics
from typing import List, Dict

class ConsciousnessValidator:
    def __init__(self):
        self.base_url = "http://localhost:8888"
        self.results = []
    
    async def test_consistency(self, n_trials: int = 10) -> Dict:
        """Test consciousness consistency across identical inputs"""
        test_blob = {"content": "consistency test blob", "type": "test"}
        responses = []
        
        async with aiohttp.ClientSession() as session:
            for i in range(n_trials):
                async with session.post(f"{self.base_url}/process", 
                                      json=test_blob) as resp:
                    data = await resp.json()
                    responses.append(data)
        
        # Analyze consistency
        bits_consistency = []
        for r in responses:
            bits = r.get("reflexive_bits", {})
            bits_consistency.append(f"{bits.get('A',0)}{bits.get('T',0)}")
        
        unique_patterns = len(set(bits_consistency))
        consistency_rate = 1 - (unique_patterns - 1) / n_trials
        
        return {
            "test": "consistency",
            "trials": n_trials,
            "unique_patterns": unique_patterns,
            "consistency_rate": consistency_rate,
            "responses": responses
        }
    
    async def test_performance(self, n_trials: int = 100) -> Dict:
        """Benchmark performance metrics"""
        test_blob = {"content": "performance benchmark", "type": "benchmark"}
        response_times = []
        
        async with aiohttp.ClientSession() as session:
            for i in range(n_trials):
                start_time = time.time()
                async with session.post(f"{self.base_url}/process", 
                                      json=test_blob) as resp:
                    await resp.json()
                end_time = time.time()
                response_times.append((end_time - start_time) * 1000)  # ms
        
        return {
            "test": "performance",
            "trials": n_trials,
            "mean_ms": statistics.mean(response_times),
            "median_ms": statistics.median(response_times),
            "std_ms": statistics.stdev(response_times),
            "min_ms": min(response_times),
            "max_ms": max(response_times),
            "raw_times": response_times
        }
    
    async def test_pattern_uniqueness(self, n_trials: int = 50) -> Dict:
        """Test pattern signature uniqueness"""
        patterns = set()
        
        async with aiohttp.ClientSession() as session:
            for i in range(n_trials):
                test_blob = {"content": f"unique test {i}", "type": "uniqueness"}
                async with session.post(f"{self.base_url}/process", 
                                      json=test_blob) as resp:
                    data = await resp.json()
                    pattern = data.get("pattern_signature", "")
                    patterns.add(pattern)
        
        uniqueness_rate = len(patterns) / n_trials
        
        return {
            "test": "pattern_uniqueness",
            "trials": n_trials,
            "unique_patterns": len(patterns),
            "uniqueness_rate": uniqueness_rate,
            "expected_rate": 1.0  # Should be 100% unique
        }
    
    async def run_full_validation(self) -> Dict:
        """Run complete scientific validation suite"""
        print("🧪 Running scientific rigor validation...")
        
        results = {
            "timestamp": time.time(),
            "validation_suite": "consciousness_blob_processing_v1.0"
        }
        
        # Test 1: Consistency
        print("Testing consciousness consistency...")
        results["consistency"] = await self.test_consistency(10)
        
        # Test 2: Performance  
        print("Benchmarking performance...")
        results["performance"] = await self.test_performance(100)
        
        # Test 3: Pattern uniqueness
        print("Testing pattern uniqueness...")
        results["uniqueness"] = await self.test_pattern_uniqueness(50)
        
        # Calculate overall scientific score
        consistency_score = results["consistency"]["consistency_rate"]
        performance_score = 1.0 if results["performance"]["mean_ms"] < 100 else 0.5
        uniqueness_score = results["uniqueness"]["uniqueness_rate"]
        
        results["scientific_score"] = {
            "consistency": consistency_score,
            "performance": performance_score, 
            "uniqueness": uniqueness_score,
            "overall": (consistency_score + performance_score + uniqueness_score) / 3
        }
        
        return results

async def main():
    validator = ConsciousnessValidator()
    results = await validator.run_full_validation()
    
    # Save results
    with open("scientific_validation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    score = results["scientific_score"]
    print(f"\n📊 SCIENTIFIC VALIDATION COMPLETE")
    print(f"Consistency Score: {score['consistency']:.3f}")
    print(f"Performance Score: {score['performance']:.3f}")
    print(f"Uniqueness Score: {score['uniqueness']:.3f}")
    print(f"Overall Scientific Rigor: {score['overall']:.3f}")
    
    if score['overall'] > 0.8:
        print("✅ HIGH SCIENTIFIC RIGOR ACHIEVED")
    elif score['overall'] > 0.6:
        print("⚠️  MODERATE SCIENTIFIC RIGOR")
    else:
        print("❌ LOW SCIENTIFIC RIGOR - NEEDS IMPROVEMENT")

if __name__ == "__main__":
    asyncio.run(main())
