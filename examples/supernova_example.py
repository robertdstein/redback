import matplotlib.pyplot as plt

import redback


sampler = 'dynesty'

model = "arnett"

sne = "SN1998bw"

data = redback.get_data.get_supernova_data_from_open_transient_catalog_data(sne)

supernova = redback.supernova.Supernova.from_open_access_catalogue(name=sne, data_mode='flux_density', active_bands=["I", "R"])
supernova.plot_multiband(filters=["I", "R", "V", "B"])

# use default priors
priors = redback.priors.get_priors(model=model)
priors['redshift'] = 1e-2
model_kwargs = dict(frequency=supernova.filtered_frequencies, output_format='flux_density')

# returns a supernova result object
result = redback.fit_model(transient=supernova, model=model, sampler=sampler, model_kwargs=model_kwargs,
                           prior=priors, sample='rslice', nlive=100, resume=True)
result.plot_corner()
result.plot_lightcurve(random_models=100, plot_others=False)
result.plot_multiband_lightcurve(filters=["I", "R", "V", "B"])#, plot_show=False)
