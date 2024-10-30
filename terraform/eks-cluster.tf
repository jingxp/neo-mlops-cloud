module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "nasa-data-cluster"
  cluster_version = "1.21"
  subnets         = ["<SUBNET_IDS>"]
  vpc_id          = "<VPC_ID>"
  node_groups = {
    nasa_nodes = {
      desired_capacity = 2
      max_size         = 3
      min_size         = 1
    }
  }
}