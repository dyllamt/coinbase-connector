## Contents

Up to date chart fields, defaults, and descriptions are documented with `helm-docs`.

## Usage

[Helm](https://helm.sh) must be installed to use the charts.  Please refer to
Helm's [documentation](https://helm.sh/docs) to get started.

Once Helm has been set up correctly, add the repo as follows:

    helm repo add cp https://dyllamt.github.io/coinbase-producer

If you had already added this repo earlier, to retrieve the latest versions of the packages:

    helm repo update cp

To see the charts:

    helm search repo cp

To install the coinbase-connector chart:

    helm install my-coinbase-producer cp/coinbase-producer

To uninstall the chart:

    helm delete my-coinbase-producer
