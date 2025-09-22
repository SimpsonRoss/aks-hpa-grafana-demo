# LLM Serving on AKS with vLLM

**Goal:** Serve open-weight LLMs (e.g. Llama-3-8B) on **Azure Kubernetes Service (AKS)** using **vLLM**.  
Focus on **latency SLOs, throughput, GPU utilization, and cost per 1k tokens**.

## Stack
- Azure AKS (GPU node pool)
- vLLM inference engine
- Prometheus + Grafana (Azure Monitor)
- GitHub Actions for CI/CD

## Planned Deliverables
- [ ] AKS GPU setup guide
- [ ] vLLM deployment YAMLs
- [ ] Prometheus metrics + Grafana dashboard JSON
- [ ] Benchmarks vs Triton
- [ ] Blog post: "Serving LLMs on AKS: vLLM vs Triton"
